
# Libraries
import os


# Versions
# 01 - Dec 30th, 2022 - Starter
# 02 - Dec 03rd, 2023 - Add functions and make it more pythonic
# 03 -


# Insights, bugfix and improvements
#


# Functions
def list_directories(path=None):
    """


    """
    if(path != None):
        os.chdir(path)

    dir_list = list()

    for f in os.listdir():
        if(os.path.isdir(f) == True):
            dir_list.append(f)


    return dir_list


def last_index(dir_list):
    """


    """
    high = 0

    for f in dir_list:
        name = f.split("-")
        index = int(name[0])

        if(index > high):
            high = index


    return high


def new_folders(start_index, n=10, verbose=True):
    """


    """
    end_index = start_index + n

    for index in range(start_index, end_index+1):
        folder_name = f"{index} - "
        os.mkdir(folder_name)

        if(verbose == True):
            print(f" > created folder: {folder_name}")


    return None
    
        
# Program --------------------------------------------------------------

dir_list = list_directories()
index = last_index(dir_list)

n = 5
new_folders(start_index=(index + 1), n=n, verbose=True)

