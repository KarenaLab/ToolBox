# [P070] Color checker

# Libraries
import os
import numpy as np

import matplotlib.pyplot as plt

# Personal libraries
from palette_source import *


# Setup/Config



# Functions
def plot_colors_palette(palette):
    """
    Function to show the colors from a given **palette**.
    
    """
    # Data preparation
    if(isinstance(palette, dict) == True):
       colors = list(palette.values())
       labels = list(palette.keys())

    elif(isinstance(palette, list) == True):
        colors = palette[:]
        labels = ["" for x in colors]

    else:
        break

    
    return None


       
