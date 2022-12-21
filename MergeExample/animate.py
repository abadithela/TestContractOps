# Create Animation for Pedestrian Crossing Example
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import glob
from PIL import Image, ImageOps
import _pickle as pickle
from matplotlib.collections import PatchCollection

TILESIZE = 100
GRID_LINES = False
START_CROSSWALK = -0.5
END_CROSSWALK = 1.5
CROSSWALK_X = 8
CROSSWALK_LOCATIONS = dict()
NUM_CW_CELLS = 8
DELTA_CW = (END_CROSSWALK-START_CROSSWALK)/NUM_CW_CELLS
for i in range(0,NUM_CW_CELLS):
    CROSSWALK_LOCATIONS.update({i: (START_CROSSWALK + i*DELTA_CW, CROSSWALK_X)})
# st()

main_dir = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))
car_figure = main_dir + '/imglib/blue_car.png'
ped_figure = main_dir + '/imglib/pedestrian_img.png'

def draw_grid():
    size = (9, 0)
    x_min = 0
    x_max = (size[0]+1) * TILESIZE
    y_min = 0
    y_max = (size[1]+1) * TILESIZE

    ax.axis('equal')
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    # fill in the road regions
    road_tiles = []
    width_tiles = np.arange(0,size[0]+1)*TILESIZE
    lanes_tiles = np.arange(0,size[1]+1)*TILESIZE
    # st()
    for i in np.arange(0,size[0]+1):
        tile = patches.Rectangle((width_tiles[i],0),TILESIZE,TILESIZE,linewidth=1,facecolor='k', alpha=0.4)
        road_tiles.append(tile)
    ax.add_collection(PatchCollection(road_tiles, match_original=True))

    # now add crosswalk on top
    crosswalk_tiles = []
    for item in CROSSWALK_LOCATIONS.keys():
        if item % 2 == 0:
            color = 'gainsboro'
            alpha = 1.0
        else:
            color = 'darkgray'
            alpha = 1.0
        width = CROSSWALK_LOCATIONS[item][1]*TILESIZE
        lanes = CROSSWALK_LOCATIONS[item][0]*TILESIZE
        tile = patches.Rectangle((width,lanes),TILESIZE,TILESIZE*DELTA_CW,linewidth=1,facecolor=color, alpha=alpha)
        crosswalk_tiles.append(tile)
    ax.add_collection(PatchCollection(crosswalk_tiles, match_original=True))

    plt.gca().invert_yaxis()

def draw_timestamp(t, merge = False):
    if merge:
        ax.text(0.5,0.7,t, transform=plt.gcf().transFigure,fontsize='large',
             bbox={"boxstyle" : "circle", "color":"white", "ec":"black"})
    else:
        ax.text(0.3,0.7,t, transform=plt.gcf().transFigure,fontsize='large',
             bbox={"boxstyle" : "circle", "color":"white", "ec":"black"})

def draw_ped(ped_data):
    if ped_data[0][1] > 0: # 0 means pedestrian is not launched yet
        x_tile = 8
        y_tile = (ped_data[0][1] - 6)
        x = (x_tile) * TILESIZE
        y = (y_tile) * DELTA_CW * TILESIZE
        # print(x)
        # print(y)
        ped_fig = Image.open(ped_figure)
        ped_fig = ped_fig.rotate(180, expand=False)
        offset = 0.1
        ax.imshow(ped_fig, zorder=1, interpolation='bilinear', extent=[x+20, x+TILESIZE-20, y+10, y+TILESIZE-10])

def draw_car(car_data):
    x_tile = car_data[0][1]
    y_tile = 0
    x = (x_tile) * TILESIZE
    y = (y_tile) * TILESIZE
    car_fig = Image.open(car_figure)
    car_fig = ImageOps.flip(car_fig)
    theta_d = 0
    car_fig = car_fig.rotate(theta_d, expand=False)
    offset = 0.1
    ax.imshow(car_fig, zorder=1, interpolation='bilinear', extent=[ x+5, x+TILESIZE-5, y+10, y+TILESIZE-10])

def animate_images(output_dir):
    # Create the frames
    frames = []
    imgs = glob.glob(output_dir+'plot_'"*.png")
    imgs.sort()
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    # Save into a GIF file that loops forever
    frames[0].save(output_dir + 'png_to_gif.gif', format='GIF',
            append_images=frames[1:],
            save_all=True,
            duration=200, loop=3)

def traces_to_animation(filename, output_dir):
    # extract out traces from pickle file
    with open(filename, 'rb') as pckl_file:
        # st()
        traces = pickle.load(pckl_file)

    t_start = 0
    t_end = len(traces)
    global ax
    fig, ax = plt.subplots()

    t_array = np.arange(t_end)
    # plot map once
    for t in t_array:
        plt.gca().cla()
        draw_grid()
        # draw_maze()
        car_data = traces[t].agent
        ped_data = traces[t].tester
        # st()
        draw_car(car_data)
        draw_ped(ped_data)
        plot_name = str(t).zfill(5)
        img_name = output_dir+'/plot_'+plot_name+'.png'
        fig.savefig(img_name, dpi=1200)
    animate_images(output_dir)

def make_animation():
    output_dir = os.getcwd()+'/animations/gifs/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    traces_file = os.getcwd()+'/saved_traces/sim_trace.p'
    traces_to_animation(traces_file, output_dir)

if __name__ == '__main__':
    make_animation()
