import os, string, random, sys, threading, time, json
from random import shuffle, randint, randrange
from Core.Py_Functions.Call import *
from Core.Py_Functions.Click import Start_Click_Processes as Start_Processes, Stop_Click_Processes as Stop_Processes, Join_All_Processes as Join_Processes
from Core.Py_Functions.GUI import Display_Border as DisplayGUI
from Core.Py_Functions.GUI import Drop_Down as DropDownGUI
from Core.Py_Functions.GUI import Character_Border as CharacterBorderGUI
from Core.Py_Functions.GUI import Character_List as CharListGUI
from Core.Py_Functions.GUI import Color_Border as ColorBorderGUI
from Core.Py_Functions.GUI import Color_List as ColorListGUI

settings = json.load(open('Core\\Settings\Settings.json'))

global max_cores
max_cores = settings['start_settings']['max_cores']
os.system("mode 72,36")

cmdwiz_out("showcursor 0")

DisplayGUI()
DropDownGUI()
CharacterBorderGUI()
CharListGUI()
ColorBorderGUI()
ColorListGUI()

if __name__ == '__main__':
    Start_Processes(max_cores)
    Join_Processes(max_cores)