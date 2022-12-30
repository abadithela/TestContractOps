# Simulated Pedestrian Crossing Example
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

import sys
sys.path.append('..')
from components.jet import Jet
from components.map import Map
from components.gridworld import GridWorld
import os
from utils import *

def new_World():
    map = Map(5,5)
    sys = [Jet('sys1', 0, 2), Jet('sys2', 4, 2)]
    tester = Jet('tester', 2, 2)
    gridworld = GridWorld(map, sys, tester)
    return gridworld, sys, tester

def run_sim(max_timestep, filepath):
    trace=[]
    gridworld, sys, tester = new_World()
    gridworld.print_gridworld()
    trace = save_scene(gridworld,trace)
    for t in range(1,max_timestep):
        print('Timestep {}'.format(t))
        gridworld.agent_take_step()
        gridworld.test_strategy()
        gridworld.print_gridworld()
        trace = save_scene(gridworld,trace)
        if gridworld.is_terminal():
            break
    save_trace(filepath, gridworld.trace)


if __name__ == '__main__':
    max_timestep = 20
    output_dir = os.getcwd()+'/saved_traces/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = 'sim_trace.p'
    filepath = output_dir + filename
    run_sim(max_timestep, filepath)
