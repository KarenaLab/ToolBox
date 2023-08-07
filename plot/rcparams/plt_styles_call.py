
# Libraries
import matplotlib.pyplot as plt


# Functions
def apply_setup(setup_dict):
    """
    Function to apply the setup dictionary.

    """
    for i in setup_dict:
        plt.rcParams[i] = setup_dict[i]

    return None


def plt_style_initial():
    """
    Main style dictionary for my personal plot.

    """
    setup_dict = {"font.family": "Helvetica",
                  "font.size": 10,
                  "figure.figsize": [8, 4.5],
                  "figure.titlesize": 10,
                  "figure.titleweight": "bold",
                  "figure.dpi": 120,
                  "savefig.dpi": 240,
                  "ps.papersize": "A4",
                  "hist.bins": "sqrt",
                  "legend.framealpha": 1,
                  "legend.fontsize": 9,
                  "xtick.direction": "inout",
                  "xtick.labelsize":9,
                  "ytick.direction": "inout",
                  "ytick.labelsize": 9,
                  "axes.titlesize": 9,
                  "axes.labelsize": 9}

    apply_setup(setup_dict)

    return None


def plt_style_no_axes():
    """
    Removing left, right and upper axes lines.

    """
    setup_dict = {"axes.spines.left": False,                  
                  "axes.spines.top": False,
                  "axes.spines.right": False,
                  "axes.spines.bottom": True,
                  "xtick.bottom": False,
                  "ytick.left": False}

    apply_setup(setup_dict)

    return None


def plt_style_boxplot():
    """
    Adjusting boxplot for bolder lines.

    """
    setup_dict = {"boxplot.notch": True,
                  "boxplot.flierprops.markerfacecolor": "darkred",
                  "boxplot.flierprops.markeredgecolor": "black",
                  "boxplot.boxprops.linewidth": 1.5,
                  "boxplot.whiskerprops.linewidth": 1.5,
                  "boxplot.capprops.linewidth": 1.5,
                  "boxplot.medianprops.linewidth": 1.5}

    apply_setup(setup_dict)

    return None


