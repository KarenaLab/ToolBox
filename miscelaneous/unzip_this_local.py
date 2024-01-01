# Unzip Folders inside me [P385]
# Unizips the .zip files at that directory (does not goes for further
# levels


# Libraries
import os
import sys
import shutil
from zipfile import ZipFile


# Personal modules
sys.path.append(r"c:\python_modules")

from file_management import *   # files_list,
#                                 folders_list and,
#                                 filter_by_extension 


# Functions
def unzip_files(path=None, delete_zip=False):
    """
    Unzip all .zip files contained in the current 

    """
    if(path != None):
        path_comeback = os.getcwd()
        os.chdir(path)

    # Read .zip files and folders
    zip_content = filter_by_extension(files_list(), files_type=[".zip"])
    folder_content = folders_list()


    # Unzip routine
    for i in zip_content:      
        name, extension = i.split(".")

        if(folder_content.count(name) == 0):
            ZipFile(i).extractall(name)
            print(f" >>> .zip file extracted: {i}")

            if(delete_zip == True):
                os.remove(i)
                print(f" >>> {i} file deleted")


    if(path != None):
        os.chdir(path_comeback)


    return None


# Program --------------------------------------------------------------
path_list = ["D:\99 - INBOX"]

for p in path_list:
    print(f" > Verifying: '{p}'")
    unzip_files(path=p, delete_zip=True)


# end
