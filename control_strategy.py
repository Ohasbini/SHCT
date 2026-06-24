

cooling_on  = 13.0   # °C, start cooling above this
cooling_off = 9.0   # °C, stop cooling below this
margin      = 2.0    # °C, ventilation only worthwhile if T_ambient < T_room - margin

idle_time = 600  # s, minimum compressor standstill before a restart
run_time  = 300  # s, minimum compressor runtime once started


class Controller:
    def __init__(self, dt: float, m_dot: float, cp: float):
 
        self._dt    = dt
        self._m_dot = m_dot
        self._cp    = cp

        self._idle_steps = idle_time / dt
        self._run_steps  = run_time / dt

        self.mode = 0
        self._comp_off_steps = self._idle_steps   # start ready to run
        self._comp_on_steps  = 0

    def step(self, T_room: float, T_ambient: float, Q_server: float) -> int:
        T_vent_floor = T_ambient + Q_server / (self._m_dot * self._cp)

        vent_useful     = T_ambient < T_room - margin    
        vent_sufficient = T_vent_floor < cooling_on     
        use_vent        = vent_useful and vent_sufficient

        comp_allowed      = self._comp_off_steps >= self._idle_steps
        must_keep_running = self.mode == 2 and self._comp_on_steps < self._run_steps

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


def mode_label(mode: int) -> str:
    return {0: "off", 1: "ventilation", 2: "AC"}[mode]