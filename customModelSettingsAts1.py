from guiScreenshots import *
from modelNames import *
import hostDB

# True = ATS1          False = ATS2
ATS = True


def AtsModel():
       if hostDB.getAtsTypeFromDB() == 1:
           ATS = True
           return ATS
       elif hostDB.getAtsTypeFromDB() == 2:
           ATS = False
           return ATS


def isLoadSizeActive(boolean):
    if boolean is False:
        while pag.locateCenterOnScreen(loadSize, confidence=0.95) is None:
            pag.scroll(300)
        findAndClick(loadSize, 5, 0.95, False)
        while pag.locateCenterOnScreen(loadSizeLabels, confidence=0.95) is None:
            pag.scroll(-400)
        findAndClickSimple(loadSizeBtnEnabled, 1, 0.95, False)


def isATS2(boolean):
    if boolean is False:
        while pag.locateCenterOnScreen(reportFormat, confidence=0.95) is None:
            pag.scroll(300)
        findAndClick(reportFormat, 3, 0.95, False)
        while pag.locateCenterOnScreen(reportFormatLabels, confidence=0.95) is None:
            pag.scroll(-300)
        if pag.locateCenterOnScreen(reportFormatLabels, confidence=0.95) is not None:
          findAndClickSimple(newOldDisabled, 1, 0.95, False)
          time.sleep(0.2)




def isWriteCurrentActive(boolean):
    if boolean is False:
        while pag.locateCenterOnScreen(writeCurrentLabelPic, confidence=0.95) is None:
            pag.scroll(300)
        findAndClick(writeCurrentLabelPic, 10, 0.95, False)
        time.sleep(0.3)
        pag.press('tab', presses=5)
        pag.press('space')


def doubleWaySwitching(boolean):
    if boolean:
        findAndClick(DWS, 5, 0.95, False)
        pag.press('up')
        pag.press('enter')
        time.sleep(0.2)
        pag.press('tab', presses=8)
        pag.press('space')
        pag.press('up')
        pag.press('enter')

def setOk():
    while pag.locateCenterOnScreen(setOKPic, confidence=0.95) is None:
        pag.scroll(-600)
    findAndClick(setOKPic, 10, 0.95, False)

def setSettings(writeCurrentActive, doubleWaySW):
 print("desde adentro de custom settings")
 isLoadSizeActive(False)
 isATS2(AtsModel())
 isWriteCurrentActive(writeCurrentActive)
 setOk()
 time.sleep(3.5)
 doubleWaySwitching(doubleWaySW)


