########################################################
#DEFINE PATH
def img(name):
    return 'modelsImg\\'+name

########MODEL FAMILIES SS#########################


class Driver():
    def __init__(self, model='', current='', ssAts1='', ssAts2="", writeCurrent=True, dwSwitch=True):
        self.model = model
        self.current = current
        self.ssAts1 = ssAts1
        self.ssAts2 = ssAts2
        self.writeCurrent= writeCurrent
        self.dwSwitch = dwSwitch

    def get_data(self):
        print("Model: "+str(self.model)+" SS_ATS1: "+str(self.ssAts1)+" SS_ATS2: "+str(self.ssAts2)+"Write Current: "+str(self.writeCurrent)+"DWSwitching: "+str(self.dwSwitch))

    def getCurrent(self):
        return self.current

    def getDWSwitch(self):
        return self.dwSwitch

#DEFINE MODEL OBJECTS

################################################################################################
#################       EUD FAMILY #######################################################

EUD075S280DT = Driver("EUD075S280DT", 3, img("EUD075S280DT_ATS1.PNG"), img("EUD075S280DT_ATS2.PNG"), True, False)

EUD150S350DTA = Driver("EUD150S350DTA", 3.7,  img("EUD150S350DTA_ATS1.PNG"),img("EUD150S350DTA_ATS2.PNG"), True, False)

EUD600S12ADT = Driver("EUD600S12ADT", 13, img("EUD600S12ADT_ATS1.PNG"), img("EUD600S12ADT_ATS2.PNG"), False, True)

EUD075S180DT = Driver("EUD075S180DT", 2, img("EUD075S180DT_ATS1.PNG"), img("EUD075S180DT_ATS2.PNG"), True, False)

EUD150S560DTA = Driver("EUD150S560DTA", 5.8, img("EUD150S560DTA_ATS1.PNG"), img("EUD150S560DTA_ATS2.PNG"), True, False)

##############################ESD FAMILY ###################################################
ESD600S12ADT = Driver("ESD600S12ADT", 13, img("ESD600S12ADT_ATS1.PNG"), img("ESD600S12ADT_ATS2.PNG"), False, True)

ESD600S12ADTF304 = Driver("ESD600S12ADTF304", 13, img("ESD600S12ADT_ATS1.PNG"), img("ESD600S12ADT_ATS2.PNG"), False, True)

ESD320S150DT = Driver("ESD320S150DT", 1.7, img("ESD320S150DT_ATS1.PNG"), img("ESD320S150DT_ATS2.PNG"), True, True)

ESD320S620DT = Driver("ESD320S620DT", 6.4, img("ESD320S620DT_ATS1.PNG"), img("ESD320S620DT_ATS2.PNG"), True, True)

ESD240S460DT = Driver("ESD240S460DT", 4.8, img("ESD240S460DT_ATS1.PNG"), img("ESD240S460DT_ATS2.PNG"), True, False)

ESD240S660DT = Driver("ESD240S660DT", 6.8, img("ESD240S660DT_ATS1.PNG"), img("ESD240S660DT_ATS2.PNG"), True, False)

ESD150S350DT = Driver("ESD150S350DT", 3.7, img("ESD150S350DT_ATS1.PNG"), img("ESD150S350DT_ATS2.PNG"), True, False)

############################## EUG FAMILY ###################################################
EUG150S350DT = Driver("EUG-150S350DT", 3.7, img("EUG150S350DT_ATS1.PNG"), img("EUG150S350DT_ATS2.PNG"), True, False)

EUG150S105DTFT02 = Driver("EUG150S105DTFT02", 1.3, img("EUG150S105DTFT02_ATS1.PNG"), img("EUG150S105DTFT02_ATS2.PNG"), True, False)
