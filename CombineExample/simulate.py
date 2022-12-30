# Simulated Pedestrian Crossing Example
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

import sys
sys.path.append('..')
from components.car import Car
from components.map import Map
from components.gridworld import GridWorld
from components.pedestrian import Pedestrian
import os
from utils import *

def new_World():
    map = Map(10, 1, 8)
    sys = Car('sys', 0, 3, 10, 'high')
    ped = Pedestrian('ped', None, 0, 8, 8)
    gridworld = GridWorld(map, sys, ped)
    return gridworld, sys, ped

def new_World_stationary_ped():
    map = Map(10, 1, 8)
    sys = Car('sys', 0, 3, 10, 'high')
    ped = Pedestrian('ped', 8, 6, 8, 8)
    gridworld = GridWorld(map, sys, ped)
    return gridworld, sys, ped

def run_stationary_pedestrian(max_timestep, filepath):
    trace=[]
    gridworld, sys, ped = new_World_stationary_ped()
    gridworld.print_gridworld()
    trace = save_scene(gridworld,trace)
    for t in range(1,max_timestep):
        print('Timestep {}'.format(t))
        gridworld.agent_take_step()
        gridworld.stationary_pedestrian()
        gridworld.print_gridworld()
        trace = save_scene(gridworld,trace)
        if gridworld.is_terminal():
            break
    save_trace(filepath, gridworld.trace)

def run_reactive_sim(max_timestep, filepath):
    trace=[]
    gridworld, sys, ped = new_World()
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
    max_timestep = 15
    output_dir = os.getcwd()+'/saved_traces/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = 'sim_trace.p'
    filepath = output_dir + filename
    run_reactive_sim(max_timestep, filepath)
    # run_stationary_pedestrian(max_timestep, filepath)
