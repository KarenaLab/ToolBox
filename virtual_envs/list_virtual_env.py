# P465 - Virtual Environments - List

# Libraries
from pathlib import Path


# Function
def list_virtualenv():
    venv_list = [str(p.parent) for p in Path.home().rglob("pyvenv.cfg")]

    if(len(venv_list) > 0):
        for v in venv_list:
            print(v)

    return venv_list


# Program --------------------------------------------------------------
if(__name__ == "__main__"):
    virtual = list_virtualenv()

    # end
    
