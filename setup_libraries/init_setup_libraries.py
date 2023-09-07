# Setup - Libraries [P010] ---------------------------------------------
# Install by script the basic libraries for a Data Scientist

# Versions
# 01 - Sept 06th, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
# 01 - Make it verbose, giving feedback of process.


# Libraries
import sys
import subprocess


# Program --------------------------------------------------------------
libraries_list = ["numpy", "pandas", "TensorFlow", "matplotlib",
                  "seaborn", "pyspark", "scikit-learn", "scipy",
                  "statsmodels", "jupyterlab", "feature-engine",
                  "xgboost", "lightgbm", "keras", "oauthlib",
                  "openpyxl"]


# Implement **pip** as a subprocess:
for lib in libraries_list:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])


# end
