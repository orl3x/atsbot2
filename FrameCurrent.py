from guiScreenshots import *
import os
import pyperclip
import time

currentStringTemplate = "CHAN 1 \\n VOLT:CURR {} \\n" \
                "CHAN 3 \\n VOLT:CURR {} \\n" \
                "CHAN 5 \\n VOLT:CURR {} \\n" \
                "CHAN 7 \\n VOLT:CURR {} \\n"

dualCurrentStringTemplate = "CHAN 1 \\n VOLT:CURR {} \\n" \
                "CHAN 5 \\n VOLT:CURR {} \\n"



def openVisaIC(current, isDualLoad):
    print(current)
    if isDualLoad:
        currentString = dualCurrentStringTemplate.format(current, current)
    else:
        currentString = currentStringTemplate.format(current, current, current, current)

    print("Current is "+str(current)+" String is "+currentString)
    pyperclip.copy(currentString)
    print(pyperclip.paste())
    os.system("taskkill -f /pid NIvisaic.exe")
    os.startfile("C://Program Files//IVI Foundation//VISA//WinNT//NIvisa//NIvisaic.exe")
    findAndClick(gpib8, 25, 0.9, True)
    findAndClick(gpibInputOutput, 5, 0.9, False)
    findAndClick(gpibEntryBox, 5, 0.9, True)
    pag.click()
    pag.write(currentString)
    findAndClick(gpibWrite, 3, 0.95, False)
    time.sleep(1.2)
    os.system("taskkill -f /pid NIvisaic.exe")





