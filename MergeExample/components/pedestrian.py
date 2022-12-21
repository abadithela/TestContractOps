# Pedestrian class
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

class Pedestrian:
    def __init__(self, name, x, s, cw_cell, goal):
        self.name = name
        self.x = x
        self.goal = goal
        self.cw_cell = cw_cell
        self.s = s
        self.go = False


    def launch(self):
        self.go = True
        self.x = self.cw_cell
        # self.take_step()

    def take_step(self):
        if self.go and not self.s == self.goal:
            self.step_forward()
        else:
            self.step_stay()

    def step_forward(self):
        self.s = self.s + 1

    def step_backward(self):
        self.s = self.s - 1

    def update_cell(self, crosswalk):
        self.cell = crosswalk[self.cwloc]

    def step_stay(self):
        pass
