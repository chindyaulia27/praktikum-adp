import os
from termcolor import colored, cprint
os.system("cls")

for i in range(10):
   cprint(" "*(10-i)*3, "white","on_white",end="")
   cprint("   "*i, "white", "on_blue",end="")
   cprint("   "*i, "white", "on_blue",end="")
   cprint(" "*(10-i)*3, "white","on_white")

for i in range(5):
   cprint("     ", "white", "on_white",end="")
   cprint("     "*10, "white", "on_light_yellow",end="")
   cprint("     ", "white", "on_white")

for i in range(4):
   cprint("     ", "white", "on_white",end="")
   cprint(" "*7, "white", "on_light_yellow",end="")
   cprint(" "*7, "white", "on_light_red",end="")
   cprint(" "*11, "white", "on_light_yellow",end="")
   cprint(" "*5, "white", "on_light_red",end="")
   cprint(" "*4, "white", "on_light_yellow",end="")
   cprint(" "*5, "white", "on_light_red",end="")
   cprint(" "*11, "white", "on_light_yellow",end="")
   cprint("     ", "white", "on_white")

for i in range(4):
   cprint("     ", "white", "on_white",end="")
   cprint(" "*7, "white", "on_light_yellow",end="")
   cprint(" "*7, "white", "on_light_red",end="")
   cprint(" "*36, "white", "on_light_yellow",end="")  
   cprint("     ", "white", "on_white") 

for i in range(6):
   cprint(" "*60, "white", "on_light_green") 