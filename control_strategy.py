

cooling_on  = 16.0   # °C, room threshold to start any cooling mode
cooling_off = 12.5   # °C, room threshold to stop cooling (hysteresis band)

AC_MUST_ON = 17.5    # °C, above this ventilation is forced off even if it was preferred

# Compressor cycling limits — protect against short-cycling, which damages the compressor
idle_time = 200  # s, minimum compressor standstill before a restart
run_time  = 300  # s, minimum compressor runtime once started


class Controller:
    def __init__(self, dt: float, m_dot: float, cp: float, cv: float, m_air_room:float):
 
        self._dt    = dt
        self._m_dot = m_dot
        self._cp    = cp
        self._cv = cv
        self._m_air_room = m_air_room

        self._idle_steps = idle_time / dt
        self._run_steps  = run_time / dt

        self.mode = 0
        self._comp_off_steps = self._idle_steps   # start ready to run
        self._comp_on_steps  = 0
        
    def server_power_estimater(self, T_room_curr: float, T_room_prev: float,
                               T_amb: float, Q_dot_AC: float,
                               mode: int, dt: float, m_air_room: float,
                               cv_air: float, cp_air: float, m_dot: float):
        # Inverts the energy balance from the previous timestep to back-calculate Q_server.
        # This lets the controller make decisions without a direct power sensor.
        if mode == 0:
            # Off: dT comes entirely from server heat → Q_server = m·cv·dT/dt
            Q_dot_server_est = m_air_room * cv_air * (T_room_curr - T_room_prev)/dt
            return Q_dot_server_est
        elif mode == 1:
            # Ventilation: dT has both server and airflow contributions → isolate server term
            Q_dot_server_est = m_air_room * cv_air * (T_room_curr - T_room_prev)/dt + m_dot * cp_air * (T_room_prev - T_amb)
            return Q_dot_server_est
        elif mode == 2:
            # AC on: dT = (Q_server + Q_AC) / (m·cv) → Q_server = m·cv·dT/dt - Q_AC
            Q_dot_server_est = m_air_room * cv_air * (T_room_curr - T_room_prev)/dt - Q_dot_AC
            return Q_dot_server_est

        return 0.0

    def step(self, T_room: float, T_ambient: float, T_room_prev: float, Q_dot_AC: float, mode_prev: int) -> int:


        # Heat added to room by ventilation airflow (negative = cooling)
        Q_dot_vent_cool = self._m_dot * self._cp * (T_ambient - T_room)  # [kW]

        Q_dot_server_est = self.server_power_estimater(T_room, T_room_prev, T_ambient, -Q_dot_AC, mode_prev, self._dt, self._m_air_room, self._cv, self._cp, self._m_dot)

        # Ventilation is deemed useful when the net room heat load (airflow + server) stays ≤ 1 kW
        vent_useful   = (Q_dot_vent_cool + Q_dot_server_est) <= 1
        AC_not_on_yet = T_room < AC_MUST_ON
        use_vent      = vent_useful and AC_not_on_yet

        # Override: if ventilation alone removes more heat than the AC can, always prefer it
        if Q_dot_vent_cool < -Q_dot_AC:
            use_vent = True

        # Override: if net load is already negative (room is cooling) and not critically hot, vent
        if (Q_dot_vent_cool + Q_dot_server_est) < 0 and T_room < AC_MUST_ON:
            use_vent = True

        comp_allowed      = self._comp_off_steps >= self._idle_steps   # idle long enough to restart
        must_keep_running = self.mode == 2 and self._comp_on_steps < self._run_steps  # protect min runtime

        if self.mode == 0:                        # off / heating up
            if T_room > cooling_on:
                if use_vent:
                    self.mode = 1
                elif comp_allowed:
                    self.mode = 2

        elif self.mode == 1:                      # ventilating
            if T_room < cooling_off:
                self.mode = 0
            elif not use_vent and comp_allowed:  
                self.mode = 2

        elif self.mode == 2:                      # AC running
            if must_keep_running:
                pass
            elif T_room < cooling_off:
                self.mode = 0
            elif use_vent:                        # free cooling became sufficient
                self.mode = 1

        if self.mode == 2:
            self._comp_on_steps  += 1
            self._comp_off_steps  = 0
        else:
            self._comp_off_steps += 1
            self._comp_on_steps   = 0

        return self.mode
