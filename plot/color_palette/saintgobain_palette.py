# Color palette --------------------------------------------------------
# Functions that returns a color palette for matplotlib graphs


def saintgobain_palette():
    """
    Returns 05 (five) colors of Saint Gobain logo.
    Source: Saint Gobain Brand Book 2024, page 20.

    """
    colors = {"green": "#00B9AA",       # RGB = 0, 185, 170
              "lightblue": "#00ADE1",  # RGB = 0, 173, 225
              "blue": "#17428C",        # RGB = 23, 66, 140
              "red": "#ED0530",         # RGB = 237, 5, 48
              "orange": "#FF7800"}      # RGB = 255, 120, 0

    return colors


def sg_palette():
    """
    Optional function for main colors, just to keep compatibility
    using the RGB information.

    """
    rgb_colors = {"green": [0, 185, 170],
                  "lightblue": [0, 173, 225],
                  "blue": [23, 66, 140],
                  "red": [237, 5, 48],
                  "orange": [255, 120, 0]}

    colors = dict()
    for name, rgb in zip(rgb_colors.keys(), rgb_colors.values()):
        info = list()
        for color in rgb:
            calc = round((color / 255), ndigits=6)
            info.append(calc)

        colors[name] = tuple(info)
        

    return colors


def sg_green_gradient(color="green", remove_40=True):
    """
    Returns the Green gradient with the removal of gradient 40
    due too closer to gradient 35 and will not be useful for
    plots.

    """
    colors = _apply_gradient(color=color, remove_40=remove_40)

    return colors


def sg_lightblue_gradient(color="lightblue", remove_40=True):
    """
    Returns the Light Blue gradient with the removal of gradient 40
    due too closer to gradient 35 and will not be useful for
    plots.

    """
    colors = _apply_gradient(color=color, remove_40=remove_40)

    return colors


def sg_blue_gradient(color="blue", remove_40=True):
    """
    Returns the Blue gradient with the removal of gradient 40
    due too closer to gradient 35 and will not be useful for
    plots.

    """
    colors = _apply_gradient(color=color, remove_40=remove_40)

    return colors


def sg_red_gradient(color="red", remove_40=True):
    """
    Returns the Red gradient with the removal of gradient 40
    due too closer to gradient 35 and will not be useful for
    plots.

    """
    colors = _apply_gradient(color=color, remove_40=remove_40)

    return colors


def sg_orange_gradient(color="orange", remove_40=True):
    """
    Returns the Orange gradient with the removal of gradient 40
    due too closer to gradient 35 and will not be useful for
    plots.

    """
    colors = _apply_gradient(color=color, remove_40=remove_40)

    return colors


def _apply_gradient(color, remove_40=True):   
    palette = sg_palette()

    gradient = dict()
    for t in _transparency(remove_40=remove_40):
        tag = f"{color}_{t}"
        info = list(palette[color])
        info.append(round((t / 100), ndigits=2))

        gradient[tag] = info

        
    return gradient


def _transparency(remove_40=True):
    """
    Returns a list of allowed transparencies for Saint Gobain colors.

    arguments:
    * remove_40 = True (removing 40 percentage because is too closer
      35 value and will not be useful for Matplotlib plots).
    
    Source: Saint Gobain Brand Book 2024, page 20.

    """
    transp = [100, 80, 60, 40, 35, 10]

    if(remove_40 == True):
        transp.remove(40)

    return transp
    
    
