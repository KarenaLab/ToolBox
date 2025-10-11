
# Libraries
import os
import sys
from zipfile import ZipFile


# Setup/Config



# Functions
def list_files(path=None):
    # Path
    path_back = os.getcwd()
    if(path != None):
        os.chdir(path)

    # Files
    files_list = list()
    for i in os.listdir():
        if(os.path.isfile(i) == True):
            files_list.append(i)


    os.chdir(path_back)


    return files_list


def filter_files(array, extension):
    # Extension preparation
    extension = extension.replace(".", "")

    files_list = list()
    for i in array:
        name, ext = os.path.splitext(i)
        ext = ext.replace(".", "")

        if(ext == extension):
            files_list.append(i)


    return files_list


def unzip_file(filename, remove_zip=False, verbose=True):
    f = ZipFile(filename, mode="r")
    f.extractall(os.getcwd())
    f.close()

    if(verbose == True):
        print(f" > file extracted {filename}")

    if(remove_zip == True):
        os.remove(filename)


    return None
    
    
# Program ---------------------------------------------------------------
if(__name__ == "__main__"):
    for i in filter_files(list_files(), extension=".zip"):
        unzip_file(i, remove_zip=True, verbose=True)

