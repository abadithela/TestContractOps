# Gridworld class
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

class GridWorld:
    def __init__(self, map, agents, tester):
        self.map = map
        self.agents = agents
        self.tester = tester
        self.timestep = 0
        self.trace = []
        self.collision = False
        self.finished = False

        self.print_gridworld()

    def print_gridworld(self):
        key_y_old = []
        for y in range(0,self.map.ys):
            printline = ""
            for x in range(0,self.map.xs):
                if self.agents[0].x == x and self.agents[0].y == y:
                        printline += 'S'
                elif self.agents[1].x == x and self.agents[1].y == y:
                        printline += 'S'
                elif self.tester.x == x and self.tester.y == y:
                    printline += 'T'
                else:
                    printline += ' '
            print(printline)

    def agent_take_step(self):
        for agent in self.agents:
            agent.agent_move()

    def test_strategy(self):
        if self.timestep == 2:
            self.confirm_switch_cw()
        if self.timestep == 10:
            self.confirm_switch_ccw()

    def confirm_switch_cw(self):
        for agent in self.agents:
            agent.switch_cw_confirm = True

    def confirm_switch_ccw(self):
        for agent in self.agents:
            agent.switch_ccw_confirm = True

    def is_terminal(self):
        is_terminal = True
        if not self.finished and not self.collision:
            is_terminal = False
        return is_terminal
