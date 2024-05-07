# Libraries
import numpy as np
import pandas as pd


filename = "iso_codes.csv"
data = pd.read_csv(filename, sep=",", encoding="utf-8")
data.loc[153, "iso_code_2"] = "NA"

data.to_csv("iso_codes_filtered.csv", index=False, sep=",", encoding="utf-8")

test = pd.read_csv("iso_codes_filtered.csv")
