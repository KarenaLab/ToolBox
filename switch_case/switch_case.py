# Name [P447] Python code to emulate switch case

# Libraries
import os
import sys


# Personal modules
sys.path.append(r"c:\python_modules")


# Functions
def zero():
    print("You typed zero")

    return None

def sqr():
    print("n is a perfect square")

    return None

def even():
    print("n is an even number")

    return None

def prime():
    print("n is a prime number")

    return None


# Setup/Config



# Program --------------------------------------------------------------
if(__name__ == "__main__"):
    options = {0: zero,
               1: sqr,
               4: sqr,
               9: sqr,
               2: even,
               3: prime,
               5: prime,
               7: prime}

    options[5]()

# end
