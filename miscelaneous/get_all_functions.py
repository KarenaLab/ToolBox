# Import modules and inspect fucntions from modules [P385]


# Versions
# 01 - Jan 24th, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import inspect



# Functions
def get_all_functions(module):
    """
    Lists ALL functions loaded by the given module.

    """
    all_func = inspect.getmembers(module, inspect.isfunction)

    name_func = list()
    for (func, _) in all_func:
        name_func.append(func)
        print(f" >>> {func}")


    return name_func


def import_list(array):
    """
    Imports ALL functions from the given list/array.

    """
    for i in array:
        try:
            modules.append(__import__(i))
            print(f" > module {i} sucessfully imported")

        except ImportError:
            print(f" > Warning: Module {i} IS NOT imported")


    return None


# end

