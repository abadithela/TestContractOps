# Helper functions
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

import sys
sys.path.append('..')
from components.scene import Scene
import _pickle as pickle

def save_trace(filename,trace): # save the trace in pickle file for animation
    print('Saving trace in pkl file')
    with open(filename, 'wb') as pckl_file:
        pickle.dump(trace, pckl_file)

def save_scene(gridworld,trace): # save each scene in trace
    print('Saving scene {}'.format(gridworld.timestep))
    sys_snapshot = []
    for agent in gridworld.agents:
        sys_snapshot.append((agent.name,agent.x, agent.y))
    tester_snapshot = []
    tester_snapshot.append((gridworld.tester.name, gridworld.tester.x, gridworld.tester.y))
    current_scene = Scene(gridworld.timestep, sys_snapshot, tester_snapshot)
    trace.append(current_scene)
    gridworld.timestep += 1
    gridworld.trace = trace
    return trace
