from multiprocessing.context import Process
import subprocess, threading, random, time
from Core.Py_Functions.Call import *
def Click_Loop ():
    global Process_Cores
    global Click_Position
    while True:
        mouse_call = subprocess.run(['Core\\fn.dll','mouse'], capture_output=True)
        Click_Position = mouse_call.stdout.decode("utf-8").split(" ")
        batbox_out(f" /g {Click_Position[1]} {Click_Position[0]} /c 0x0c /a 88")
    return

def Start_Click_Processes (max_cores: int):
    global Process_Cores
    Process_Cores = []
    for i in range(max_cores):
        Process_Cores.append(Process(target=Click_Loop))
    for i in range(max_cores):
        Process_Cores[i].start()
    return

def Stop_Click_Processes (max_cores):
    global Process_Cores
    for i in range(max_cores):
        Process_Cores[i].kill()
    Process_Cores = []
    return

def Join_All_Processes (max_cores):
    global Process_Cores
    for i in range(max_cores):
        Process_Cores[i].join()
    return
        