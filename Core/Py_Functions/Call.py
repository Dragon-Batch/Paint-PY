import os, subprocess

def batbox_out (command: str):
    os.system(f"Core\\batbox.exe {command}")
    return

def batbox_return (command: str):
    return(os.popen(f"Core\\batbox.exe {command}"))

def fndll_out (command: str):
    os.system(f"Core\\fn.dll {command}")
    return

def fndll_return (command: str):
    return(os.popen(f"Core\\fn.dll {command}"))

def cmdwiz_out (command: str):
    os.system(f"Core\\cmdwiz.exe {command}")
    return

def cmdwiz_return (command: str):
    return(os.popen(f"Core\\cmdwiz.exe {command}"))
