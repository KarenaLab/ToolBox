# Setup - Libraries [P010] ---------------------------------------------
# Check installed libraries

# Versions
# 01 - Sept 06th, 2023 - Starter
# 02 -


# Insights, improvements and bugfix

# Libraries
import sys
import subprocess


# Program --------------------------------------------------------------
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])

# Process data
installed_packages = [r.decode().split("==")[0] for r in reqs.split()]


# Print it
for i in installed_packages:
    print(i)

