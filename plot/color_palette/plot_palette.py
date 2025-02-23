# [P070] Color checker

# Libraries
import os
import numpy as np

import matplotlib.pyplot as plt

# Personal libraries
from palette_source import *


# Setup/Config



# Functions
def plot_palette(palette, title=None, savefig=False, verbose=True):
    """
    Function to show the colors from a given **palette**.
    
    """
    # Data preparation
    if(isinstance(palette, dict) == True):
       colors = list(palette.values())
       labels = list(palette.keys())
       labels = zip_name(labels, colors)
       values = [1 for x in colors]

    elif(isinstance(palette, list) == True):
        colors = palette[:]
        labels = ["" for x in colors]
        labels = zip_name(labels, colors)
        values = [1 for x in colors]

    else:
        return None

    # Title
    if(title == None):
        title = "Palette colors viz"

    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.major.size"] = 0
    plt.rcParams["ytick.major.size"] = 0

    # Figure
    fig = plt.figure(figsize=[8, 4.5])  # Widescreen [16:9]
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")
    ax = plt.axes()
    
    plt.bar(labels, height=values, bottom=0, color=colors)

    # Remove axes and ylabels
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.spines.left.set_visible(False)
    ax.spines.bottom.set_visible(False)
    plt.yticks(ticks=[0, 1], labels=["", ""])
    
    

    # Printing
    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=320)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()

    plt.close(fig)

    return None


def zip_name(labels, colors):
    names = list()

    for (l, c) in zip(labels, colors):
        tag = f"{l}\n{c}"
        names.append(tag)

    return names
        

# Program
if(__name__ == "__main__"):
    savefig = True
    plot_palette(samsung_palette(), title="Samsung palette", savefig=savefig)
    plot_palette(saintgobain_palette(), title="Saint Gobain palette", savefig=savefig)
