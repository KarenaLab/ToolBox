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
libraries_list = ["numpy", "pandas",
                  "scikit-learn", "scipy", "statsmodels", "feature-engine",
                  "scikit-posthocs",
                  "xgboost", "lightgbm",
                  "TensorFlow", "keras",
                  "matplotlib", "seaborn", "plotly",
                  "pyspark", "jupyterlab", "oauthlib", "openpyxl",
                  "PyGithub", "ml-metadata"]


# Implement **pip** as a subprocess:
for lib in libraries_list:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
    print(f' > Library "{lib}" installed sucessfully.')


# end
