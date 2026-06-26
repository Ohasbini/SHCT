

cooling_on  = 16.0   # °C, start cooling above this
cooling_off = 12.5   # °C, stop cooling below this
margin      = 1.0    # °C, ventilation only worthwhile if T_ambient < T_room - margin

AC_MUST_ON = 17.5


idle_time = 150  # s, minimum compressor standstill before a restart
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
                               cv_air: float, cp_air: float, m_dot: float) -> float:
        
        if mode == 0:
            return m_air_room * cv_air * (T_room_curr - T_room_prev) / dt
        
        elif mode == 1:
            return m_air_room * cv_air * (T_room_curr - T_room_prev) / dt + m_dot * cp_air * (T_room_prev - T_amb)
        
        elif mode == 2:
            return m_air_room * cv_air * (T_room_curr - T_room_prev) / dt - Q_dot_AC
        
        return 0.0 

    def step(self, T_room: float, T_ambient: float, Q_server: float, T_room_prev: float, Q_dot_AC: float, mode_prev: int) -> int:

  

        Q_dot_vent_cool = self._m_dot * self._cp * (T_ambient - T_room) #[kW]
        
        Q_dot_server_est = self.server_power_estimater(T_room, T_room_prev, T_ambient, -Q_dot_AC, mode_prev, self._dt, self._m_air_room, self._cv, self._cp, self._m_dot)
        
        
        vent_useful     = T_ambient < T_room - margin
        
        vent_useful =   (float(Q_dot_vent_cool) + Q_dot_server_est) <= 1
        #vent_sufficient = T_vent_floor < cooling_on    
        vent_sufficient = 1 
        AC_not_on_yet = T_room < AC_MUST_ON
        use_vent        = vent_useful and vent_sufficient and AC_not_on_yet
        
        if Q_dot_vent_cool < -5:
            use_vent = True
            
        if (Q_dot_vent_cool + Q_dot_server_est) < 0:
            use_vent = True

        comp_allowed      = self._comp_off_steps >= self._idle_steps
        must_keep_running = self.mode == 2 and self._comp_on_steps < self._run_steps

        if self.mode == 0:                        # off / heating up
            if T_room > cooling_on:
                if use_vent:
                    self.mode = 1
                elif comp_allowed:
                    self.mode = 2

        elif self.mode == 1:                      # ventilating
            if T_room < cooling_off :
                self.mode = 0
            elif not use_vent and comp_allowed:  
                self.mode = 2

        elif self.mode == 2:                      # AC running
            if must_keep_running:
                pass
            elif T_room < cooling_off :
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


def mode_label(mode: int) -> str:
    return {0: "off", 1: "ventilation", 2: "AC"}[mode]