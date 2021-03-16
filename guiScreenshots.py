import pyautogui as pag
import time
import os
def img(name):
    return 'guiImg\\'+name

botTestFilesPic = img("botTestFiles.PNG")
ATS1FolderPic= img("ATS1.PNG")
ATS2FolderPic = img("ATS2.PNG")
mesIconPic = img("mesShortcut.png")
mesUpdateOkButton = img("mesUpdateOkButton.png")
mesLoginBtnPic = img("mesLoginBtn.png")
emptyLoginWindow = img("emptyLoginWindow.PNG")
userNameEntry = img("userNameEntry.PNG")
passwordEntry = img("passwordEntry.PNG")
mesSideMenuBtnPic = img("mesSideMenuBtn.png")
startWorkingSideMenuPic = img("startWorkingSideMenu.PNG")
blueOKbtnPic = img("blueOKbtn.PNG")
processScanSearchPic = img("processScanSearch.PNG")
processScanSearchTextBoxPic = img("processScanSearchTextBox.PNG")
mesSearchBtnPic = img("mesSearchBtn.PNG")
atsShortcutPic = img("atsShortcut.PNG")
runBtnPic = img("runBtn.PNG")
inventronicsLogoPic = img("inventronicsLogo.PNG")
settingsBtnPic =img("settingsBtn.PNG")
barcodeLabelPic = img("barcodeLabel.PNG")
folderTestFilePic = img("folderTestFile.PNG")
atsOpenBtnPic = img("atsOpenBtn.PNG")
writeCurrentLabelPic = img("writeCurrentLabel.PNG")
setOKPic = img("setOK.PNG")
DWS = img("doyebleWaySwitching.PNG")
loadSize= img("loadSize.PNG")
loadSizeLabels = img("loadSizeLabels.PNG")
loadSizeBtnEnabled = img("loadSizeBtnEnabled.PNG")
reportFormat = img("reportFormat.PNG")
newOldDisabled = img("newOldDisabled.PNG")
reportFormatLabels = img("reportFormatLabels.PNG")

# FRAME CURRENT SCREENSHOTS
gpib8 = img("GPIB8.PNG")
gpibInputOutput = img("gpibInputOutput.PNG")
gpibEntryBox = img("gpibEntryBox.PNG")
gpibWrite = img("gpibWrite.PNG")
gpibNoError = img("gpibNoError.PNG")



def showDesktop():
    pag.hotkey('win','d')

def mesNeedsLogin(boolean):
    if boolean:
        findAndClick(userNameEntry, 3, 0.95, False)
        pag.write("001864")
        findAndClick(passwordEntry, 3, 0.95, False)
        pag.write("001864")
    print('False')

def findAndClickSimple(img, timeLimit, conf, doubleClick):
    cords = None
    timeLimit = (timeLimit/0.4)
    i = timeLimit
    while cords is None:
     if i > 0:
        i=i-1
        cords = pag.locateCenterOnScreen(img, confidence=conf)
        time.sleep(0.2)
     else:
         print('Out')
         break

    if doubleClick:
         pag.doubleClick(cords)
    else:
         pag.click(cords)

def findAndClick(img, timeLimit, conf, doubleClick):
    cords = None
    timeLimit = (timeLimit/0.4)
    i = timeLimit
    while cords is None:
     if i > 0:
        i=i-1
        cords = pag.locateCenterOnScreen(img, confidence=conf)
        time.sleep(0.2)
     else:
         print('Out')
         pag.alert("Ocurrio un error, solicite apoyo al técnico de pruebas")
         exit()

    if doubleClick:
         pag.doubleClick(cords)
    else:
         pag.click(cords)

def findAndBool(img, timeLimit, conf):
    cords = None
    timeLimit = (timeLimit/0.4)
    i = timeLimit
    while cords is None:
     if i > 0:
        i=i-1
        cords = pag.locateCenterOnScreen(img, confidence=conf)
        time.sleep(0.2)
     else:
         print('Out')
         pag.alert("An error ocurred")
         exit()

     return True




def killTasks():
    os.system("taskkill /im MES(MEXICO).exe -f")
    os.system('taskkill /im "ATS For Mexico.exe" -f')