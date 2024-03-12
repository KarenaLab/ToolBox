### The Rules
-----

#### Introduction
A very direct rules that drives coding, it is a collection of best practices for a better coding.
Before your critics (thing that I would love to hear, because I am sure will improve this rules), just consider that this rules are focused in a Data Scientist focused more in experiments, tests, tunning and modeling than MLOps and production.

I will try to join rules by groups to make easier connection and to find guidance when it is need

#### Rules - Generic
1. Follow [PEP-008](https://peps.python.org/pep-0008/) and [Numpy Docstrings](https://numpydoc.readthedocs.io/en/latest/format.html) as much you could and when there is not a explicit rule for the topic,

2. Import conventions
	1. Import all libraries and needs in the beginning of the script,
	2. Adopt some import conventions to avoid conflict between scripts that could be running simultaneously,
	3. Avoid wild cards import,
	4. Sequence to import:
		* python libraries
		* Full library: numpy, pandas, scipy.stats and matplotlib.pyplot
		* Single function: When import a single function, importe by sequence of use
		* Tools: Personal tools made exclusive for the application/experiment and local (or common) tools from the `python_modules`.

3. ononon

Example of import
```
# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

from personal_tools import * 			# Avoid wild cards import.
```

#### Rules - Data Science
1. All information traffic and storage by numpy,
2. Results and metrics as namedtuple or dictionary,
3. 

#### Rules - Numpy


#### Rules - Pandas


#### Rules - Matplotlib


-----
#### Statistics
* Date: Mar 06th, 2024
* Version: 01





