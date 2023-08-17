
import colorama
from colorama import Fore, Back, Style

# Source
# https://pypi.org/project/colorama/


colorama.init(autoreset=True)

print(Fore.BLUE + "Testing Blue")
print(Fore.GREEN + "Testing Green")
print(Fore.CYAN + "Testing Cyan")
print(Fore.MAGENTA + "Testing Magenta")
print(Fore.RED + "Testing Red")

print("This is a simple plot")
print(Fore.WHITE + "Testing WHITE color and comparing with Normal print")
print(Fore.BLUE + Style.DIM +Back.WHITE + "Testing Blue with dimmer version and WHITE background")

print(Fore.YELLOW + Style.DIM +"Testing Yellow sun DIM")
print(Fore.YELLOW + "Testing Yellow sun NORMAL")
print(Fore.YELLOW + Style.BRIGHT + "Testing Yellow sun BRIGHT")

