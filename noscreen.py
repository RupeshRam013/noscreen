
"""
# Text for the developers and programmers who are seeking 
  for additional information

--NoScreen:
  A small python script capable to store the screenshots of the user in given time period with the quantity provided to the script .

--Working:
  This program uses the module "PYSCREENSHOT" for capturing and saving the screen shots .The time module defines the time period , os handles the directory and files for the script and the sys obtains the arguments .

--Creator:
  The creator of this script : @Rupeshram013

--Note:
  This program is just a fun project and don't expect anything big from this puny project but this might be helpful for some people only .
"""



#Libraries for the script
import pyscreenshot as lens
import os
import time
import sys
from colorama import *

print("Welcome to program ;")
print()
print(Fore.BLUE+"_     _    __                                  ")
print(Fore.BLUE+"| \    |   |       |       __     __    __        __   __   _    _")
print(Fore.BLUE+"|   \  |   |       |     ( _      |        |__)     |__  |__  |  \  |")
print(Fore.BLUE+"|     \|   | __ |      __)   |__   |     \     |__  |__  |    \|")

print()

print(Fore.WHITE+"A program that can take screenshots for users with given time period and quantity ;")
print("Created by : @RupeshRam013")
print()
print(Fore.RED+"Please follow the following syntax ;\n")
print(Fore.GREEN + "Time : (t0) : <syntax> python3 noscreen.py t10")
print("Rate : (R0) : <syntax> python3 noscreen.py r10")
print("Path : (./Path): <syntax> python3 noscreen.py ./images")
print(Fore.RED + "Full Arguments : <syntax> python3 noscreen.py t20 r30 ./images")

#The memory location for major data
allargv = sys.argv
PathForImg = None
TimeForImg = 0
RateForImg = 1
paths = os.listdir()


#Extracts the required values from the arguments provided
if len(allargv) != 4:
   pass
else:
   for r in range(0,len(allargv)):
      if allargv[r][0:2] == "./":
         PathForImg = allargv[r]
      elif allargv[r][0:1].upper() == "T":
         TimeForImg = int(allargv[r][1:])   
      elif allargv[r][0:1].upper() == "R":
         RateForImg = int(allargv[r][1:])
      

#Clears and defines and proper directory for storing the data
if PathForImg:
   for i in range(0,len(paths)):
      if os.path.isdir(paths[i]):
         os.chdir(paths[i])

         allimg = os.listdir()

         for j in range(0,len(allimg)):
            if os.path.isdir(allimg[j]):
               os.rmdir(allimg[j])
            else:
               os.remove(allimg[j])

         os.chdir("../")
         os.rmdir(paths[i])

      elif paths[i][-3:] != ".py":
         os.remove(paths[i])

   os.mkdir(PathForImg)


#Capturing and storing the images in the paths provided
if len(allargv) != 4:
   print(Fore.RED + "\nPlease provide the required arguments ;")
else: 
   print(Fore.WHITE + "\nCapturing and saving the screenshots.....")
   for u in range(0,RateForImg):
      time.sleep(TimeForImg)
      AltImg = lens.grab()
      imgname = "img-0" + str(u) + ".png"
      AltImg.save(f"{PathForImg}/{imgname}")









