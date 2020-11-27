# RP-Dice-Roll-RNG
 This repo is for those people who play DnD or CoD (Chronicles of Darkness, not Call Of Duty) this is a automatic dice roller for all you tabletop games people
 
 # How to contribute
 I would appreciate if you left the .exe building to me so i can handle dependency changes and what not, but if you want to use the venv (not implemented yet) and do the dependency work yourself, feel free. I implore you to **test** your code before you commit it please
 
# How to build the exe
 To build the exe, download pyinstaller with the below shell command for windows:
 ```pip install pyinstaller```
for Linux:
 ```pip3 install pyinstaller```
 once you have installed Pyinstaller, open a shell window in the same directory the source code is in, and run this script (any OS)
 ```pyinstaller --onefile rpdiceroll.py```
