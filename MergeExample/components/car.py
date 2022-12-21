# Car (system under test) class
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

class Car:
    def __init__(self, name, x, v, goal, vis):
        self.name = name
        self.x = x
        self.v = v
        self.goal = goal
        # self.orientation = orientation
        self.breaking = False
        self.v_max = 4
        self.v_min = 0
        self.vis = vis

    def agent_move(self, ped_in_cell):
        self.car_strategy(ped_in_cell)

    def detect_pedestrian(self, ped_in_cell):
        if ped_in_cell:
            if self.vis == 'high':
                if ped_in_cell <= self.x + 5:
                    self.breaking = True
            if self.vis == 'low':
                if ped_in_cell <= self.x + 2:
                    self.breaking = True

    def car_strategy(self, ped_in_cell):
        self.detect_pedestrian(ped_in_cell)
        if not self.breaking:
            self.step_constant_forward()
        else:
            self.step_decelerate()

    def step_constant_forward(self):
        # self.x = self.x + self.v
        self.x = self.x + 1

    def step_decelerate(self):
        if self.v > self.v_min:
            self.v = self.v-1
        # self.x = self.x + self.v
        if self.v > 0:
            self.x = self.x + 1

    def step_accelerate(self):
        if self.v < self.v_max:
            self.v = self.v+1
        self.x = self.x + self.v

    def step_stay_stopped(self):
        self.v = 0
        self.x = self.x
