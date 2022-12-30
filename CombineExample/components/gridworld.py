# Gridworld class
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

class GridWorld:
    def __init__(self, map, agent, tester):
        self.map = map
        self.agent = agent
        self.tester = tester
        self.timestep = 0
        self.trace = []
        self.collision = False

        self.print_gridworld()

    def print_gridworld(self):
        key_y_old = []
        printline = ""
        for x in range(0,self.map.xs):
            if self.agent.x == x:
                printline += 'S'
            elif self.tester.x == x:
                printline += 'P'
            else:
                printline += ' '
        print(printline)

    def agent_take_step(self):
        self.agent.agent_move(self.tester.x)

    def test_strategy(self):
        if self.agent.x >= 5 and not self.tester.go: # if not yet launched - launch the pedestrian
            self.launch_pedestrian()
        self.tester.take_step() # will only step forward if it was launched

    def launch_pedestrian(self):
        self.tester.launch()

    def stationary_pedestrian(self):
        self.tester.step_stay()

    def is_terminal(self):
        terminal = False
        if self.agent.x == self.agent.goal or self.collision:
            terminal = True
        return terminal
