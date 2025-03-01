# [P070] Colors palette -------------------------------------------------

# Source of color palettes to be used with Matplolib and other data
# visualization libraries baes on,

def hex_to_rgb(hex_code):
    """
    Convert an hexadecimal code into RGB components.

    """
    # Data preparation
    hex_code = hex_code.replace("#", "")

    # Split hex color into Red, Green and Blue (RGB) components
    rgb = tuple(int(hex_code[i: i+2], 16) for i in (0, 2, 4))


    return rgb

    
def black_scale():
    """
    Returns a dict with 5 colors with black gradient.
    
    """
    colors = {"black_1": "lightgrey",
              "black_2": "darkgrey",
              "black_3": "grey",
              "black_4": "dimgrey",
              "black_5": "black"}

    return colors


def grey_scale():
    """
    Returns a dict with 5 colors with grey gradient.
    
    """
    colors = {"grey_1": "whitesmoke",
              "grey_2": "lightgrey",
              "grey_3": "darkgrey",
              "grey_4": "grey",
              "grey_5": "dimgrey"}

    return colors


def blue_scale():
    """
    Returns a dict with 5 colors with blue gradient.
    
    """
    colors = {"blue_1": "aliceblue",
              "blue_2": "lightsteelblue",
              "blue_3": "cornflowerblue",
              "blue_4": "royalblue",
              "blue_5": "navy"}

    return colors


def green_scale():
    """
    Returns a dict with 5 colors with green gradient.
    
    """
    colors = {"green_1": "honeydew",
              "green_2": "lightgreen",
              "green_3": "yellowgreen",
              "green_4": "olivedrab",
              "green_5": "darkgreen"}

    return colors


def red_scale():
    """
    Returns a dict with 5 colors with red gradient.
    
    """
    colors = {"red_1": "mistyrose",
              "red_2": "lightcoral",
              "red_3": "indianred",
              "red_4": "firebrick",
              "red_5": "darkred"}

    return colors


def yellow_scale():
    """
    Returns a dict with 5 colors with yellow gradient.
    
    """
    colors = {"yellow_1": "lightyellow",
              "yellow_2": "cornsilk",
              "yellow_3": "bisque",
              "yellow_4": "wheat",
              "yellow_5": "orange"}

    return colors       


def bic4_scale():
    """
    Returns a dict with 5 colors with yellow gradient.
    
    """
    colors = {"blue": "navy",
              "red": "darkred",
              "yellow": "orange",
              "green": "darkgreen",
              "black": "black"}

    return colors


def samsung_palette():
    """
    Returns a dict with 6 colors with Samsung pallete.
    (( Suggests to use carefully blue_acqua ))
    
    """
    colors = {"blue_main": "#1428A0",      # r=020, g=040, b=160
              "blue_light": "#0077C8",     # r=000, g=199, b=200
              "blue_aqua": "#00C3B2",      # r=000, g=195, b=178
              "green": "#97D653",          # r=151, g=214, b=083
              "orange": "#FFB546",         # r=255, g=181, b=070
              "red": "#FF4337"}            # r=255, g=067, b=055

    return colors


def saintgobain_palette():
    """
    Returns 05 (five) colors of Saint Gobain logo.
    Source: Saint Gobain Brand Book 2024, page 20.

    """
    colors = {"green": "#00B9AA",       # RGB = 0, 185, 170
              "lightblue": "#00ADE1",   # RGB = 0, 173, 225
              "blue": "#17428C",        # RGB = 23, 66, 140
              "red": "#ED0530",         # RGB = 237, 5, 48
              "orange": "#FF7800"}      # RGB = 255, 120, 0

    return colors


def economist_palette():
    """
    Returns 08 (eight) colors for plots with The Economist style.

    """
    colors = {"red": "#DB444B",
              "blue": "#006BA2",
              "cyan": "#3EBCD2",
              "green": "#379A8B",
              "yellow": "#EBB434",
              "olive": "#B4BA39",
              "purple": "#9A607F",
              "gold": "#D1B07C"}

    return colors


def romania_palette():
    """
    Returns a dict with 5 colors with main colors= Blue, Red and Yellow.
    For this reason, called Romania.
    
    Source: https://coolors.co/palette/003049-d62828-f77f00-fcbf49-eae2b7

    """
    colors = {"darkblue": "#003049",
              "red": "#D62828",
              "orange": "#F77F00",
              "yellow": "#FCBF49",
              "sand": "#EAE2B7"}

    return colors


def france_palette():
    """
    Returns a dict with 4 colors with main colors= Blue, Red and white.
    For this reason, called France.
    
    Source: https://coolors.co/palette/e63946-f1faee-a8dadc-457b9d-1d3557
    """

    colors = {"red": "#E63946",
              "blue_light": "#A8DADC",
              "blue_middle": "#457B9D",
              "blue_dark": "#1D3557"}

    return colors


def nbc_palette():
    """
    Returns a dict with 6 colors with NBC logo palette.
    Good pastel tone palette.

    """
    colors = {"blue": "#0089D0",
              "red": "#CC004C",
              "green": "#0DB14B",
              "yellow": "#FCB711",
              "purple": "#6460AA",
              "orange": "#F37021"}

    return colors


def spring_pastels():
    """
    Returns a dict with 9 pastel colors palette.
    Source: https://www.heavy.ai/blog/12-color-palettes-for-telling-better-stories-with-your-data

    """
    colors: {"red": "#fd7f6f",
             "blue": "#7eb0d5",
             "green": "#b2e061",
             "purple": "#bd7ebe",
             "orange": "#ffb55a",
             "yellow:": "#ffee65",
             "purple2": "#beb9db",
             "pink": "#fdcce5",
             "aqua": "#8bd3c7"}

    return colors


def blue2red_palette():
    """
    Returns a dict with 09 (nine) pastel colors palette from blue to red.
    Source: https://www.heavy.ai/blog/12-color-palettes-for-telling-better-stories-with-your-data

    """   
    colors = {"blue_1": "#1984c5",
              "blue_2": "#22a7f0",
              "blue_3": "#63bff0",
              "blue_4": "#a7d5ed",
              "grey": "#e2e2e2",
              "red_4": "#e1a692",
              "red_3": "#de6e56",
              "red_2": "#e14b31",
              "red_1": "#c23728"}

    return colors


def blue_gradient():
    """
    Returns a dict with 05 (five) blue gradient colors.

    """
    colors = {"blue_01": "#011f4b",     # (1,31,75) rgb
	      "blue_02": "#03396c",	# (3,57,108)
	      "blue_03": "#005b96",	# (0,91,150)
 	      "blue_04": "#6497b1",     # (100,151,177)
              "blue_05": "#b3cde0"}	# (179,205,224)

    return colors


def fitzpatrick_gradient():
    """
    Returns 06 (six) Fitzpatrick skin tones as color gradient.

    """

    colors = {"fs1": "#FEFEFE",     # r=254, g=254, b=254
              "fs2": "#FBEED2",     # r=251, g=238, b=210
              "fs3": "#EACD79",     # r=234, g=205, b=121
              "fs4": "#D7A306",     # r=215, g=163, b=006
              "fs5": "#96734E",     # r=150, g=115, b=078
              "fs6": "#6E3B07"}     # r=110, g=059, b=007

    return colors


def microsoft_palette():
    """
    Returns 05 (five) colors of Microsoft logo.

    """
    colors = {"orange": "#F25022",
              "green": "#7FBA00",
              "blue": "#00A4EF",
              "yellow": "#FFB900",
              "grey": "#737373"}

    return colors


# end
