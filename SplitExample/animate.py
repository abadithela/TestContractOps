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
from ipdb import set_trace as st

TILESIZE = 100

main_dir = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))
blue_jet_figure = main_dir + '/imglib/blue_jet.png'
red_jet_figure = main_dir + '/imglib/red_jet.png'
tester_jet_figure = main_dir + '/imglib/tester_jet.png'

def draw_grid():
    size = (5, 5)
    x_min = 0
    x_max = (size[0]) * TILESIZE
    y_min = 0
    y_max = (size[1]) * TILESIZE

    # ax.axis('equal')
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    # fill in the regions
    tiles = []
    width_tiles = np.arange(0,size[0])*TILESIZE
    lanes_tiles = np.arange(0,size[1])*TILESIZE
    # st()
    for i in np.arange(size[1]):
        for k in np.arange(size[0]):
            tile = patches.Rectangle((width_tiles[k],lanes_tiles[i]),TILESIZE,TILESIZE,linewidth=1,facecolor='lightsteelblue', edgecolor='darkgray', alpha=0.4)
            tiles.append(tile)
    ax.add_collection(PatchCollection(tiles, match_original=True))

    plt.gca().invert_yaxis()

def draw_timestamp(t, merge = False):
    if merge:
        ax.text(0.5,0.7,t, transform=plt.gcf().transFigure,fontsize='large',
             bbox={"boxstyle" : "circle", "color":"white", "ec":"black"})
    else:
        ax.text(0.3,0.7,t, transform=plt.gcf().transFigure,fontsize='large',
             bbox={"boxstyle" : "circle", "color":"white", "ec":"black"})

def draw_jet(jet_data, color_fig):
    x_tile = jet_data[1]
    y_tile = jet_data[2]
    x = (x_tile) * TILESIZE
    y = (y_tile) * TILESIZE
    jet_fig = Image.open(color_fig)
    jet_fig = ImageOps.flip(jet_fig)
    theta_d = 0
    jet_fig = jet_fig.rotate(theta_d, expand=False)
    offset = 0.1
    ax.imshow(jet_fig, zorder=1, interpolation='bilinear', extent=[ x+5, x+TILESIZE-5, y+20, y+TILESIZE-20])

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
        jet_data = traces[t].agents
        tester_data = traces[t].tester
        draw_jet(jet_data[0], blue_jet_figure)
        draw_jet(jet_data[1], red_jet_figure)
        draw_jet(tester_data[0], tester_jet_figure)
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
