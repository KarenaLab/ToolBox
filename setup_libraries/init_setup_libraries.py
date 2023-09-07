import sys
import subprocess


# implement pip as a subprocess:
libraries_list = ["numpy", "pandas", "TensorFlow", "matplotlib", "seaborn",
                  "pyspark", "scikit-learn", "scipy", "statsmodels", "jupyterlab",
                  "feature-engine", "xgboost", "lightgbm"]

for lib in libraries_list:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
