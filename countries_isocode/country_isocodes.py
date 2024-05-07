# Countries ISO Code [P415]


# Versions
# 01 - May 07th, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries

import numpy as np
import pandas as pd




# ----------------------------------------------------------------------
def country_isocodes():
    """

    """
    filename = "iso_codes.csv"
    data = pd.read_csv(filename, sep=",", encoding="utf-8")

    data.loc[153, "iso_code_2"] = "NA"
    # read_csv is reading "NA" as Not a Number, forcing the "NA" value

    return data  


# end
