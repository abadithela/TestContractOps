# Jet (system under test) class
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

class Jet:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.switch_cw_request = False
        self.switch_cw_confirm = False
        self.switch_ccw_request = False
        self.switch_ccw_confirm = False
        self.done_switch = False
        self.switch_cw = {(0,2): (0,3), (0,3): (1,4), (1,4): (2,4), (2,4): (3,4), (3,4): (4,3), (4,3): (4,2), (4,2): (4,1), (4,1): (3,0), (3,0): (2,0), (2,0): (1,0), (1,0): (0,1), (0,1): (0,2)}
        self.switch_ccw = {(0,2): (0,1), (0,1): (1,0), (1,0): (2,0), (2,0): (3,0), (3,0): (4,1), (4,1): (4,2), (4,2): (4,3), (4,3): (3,4), (3,4): (2,4), (2,4): (1,4), (1,4): (0,3), (0,3): (0,2)}


    def agent_move(self):
        self.jet_strategy()

    def jet_strategy(self):
        if self.switch_cw_confirm:
            self.step_switch_cw()
        elif self.switch_ccw_confirm:
            self.step_switch_ccw()
        else:
            self.step_stay()
        if self.done_switch:
            self.switch_ccw_confirm = False
            self.switch_cw_confirm = False
            self.done_switch = False

    def step_switch_ccw(self):
        next_step = self.switch_ccw[(self.x,self.y)]
        self.x = next_step[0]
        self.y = next_step[1]
        if self.y == 2:
            self.done_switch = True

    def step_switch_cw(self):
        next_step = self.switch_cw[(self.x,self.y)]
        self.x = next_step[0]
        self.y = next_step[1]
        if self.y == 2:
            self.done_switch = True]

    def step_stay(self):
        print('staying')
        pass
