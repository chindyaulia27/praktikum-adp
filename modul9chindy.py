import os
from termcolor import colored, cprint

os.system("cls")
cprint("  ", "white","on_grey")
for i in range (5):
   cprint(" "*2, "white","on_grey", end="")
   cprint(" "*40, "white","on_red")

for j in range (6):
    cprint(" "*2, "white","on_grey", end="")
    cprint(" "*40,"white","on_white")

for j in range (12):
    cprint(" "*2, "white","on_grey")

