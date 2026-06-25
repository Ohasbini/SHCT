cooling_on = 17.0          # cooling on above this
cooling_off = 15.0         # cooling off below this
margin = 2.0    # T_ambient < T_room - margin

# compressor timing timesteps
idle_time = 2   
run_time = 1      


class Controller:
    def __init__(self):
        self.mode = 0
        self._comp_off_steps = idle_time 
        self._comp_on_steps = 0

    def step(self, T_room: float, T_ambient: float) -> int:
        vent_on = T_ambient < T_room - margin
        comp_allowed = self._comp_off_steps >= idle_time
        must_keep_running = self.mode == 2 and self._comp_on_steps < run_time

        if self.mode == 0:
            if T_room > cooling_on:
                if vent_on:
                    self.mode = 1
                elif comp_allowed:
                    self.mode = 2

        elif self.mode == 1:
            if T_room < cooling_off:
                self.mode = 0
            elif not vent_on and comp_allowed:
                self.mode = 2

        elif self.mode == 2:
            if must_keep_running:
                pass 
            elif T_room < cooling_off:
                self.mode = 0
            elif vent_on:
                self.mode = 1

        if self.mode == 2:
            self._comp_on_steps += 1
            self._comp_off_steps = 0
        else:
            self._comp_off_steps += 1
            self._comp_on_steps = 0

        return self.mode


def mode_label(mode: int) -> str:
    return {0: "off", 1: "ventilation", 2: "AC"}[mode]
