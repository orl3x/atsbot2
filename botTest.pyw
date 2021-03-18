import pyperclip
import tkinter as tk
import tkinter.ttk as ttk
from customModelSettingsAts1 import *
import modelsDB
import FrameCurrent
import re


guiPasswords = {'201101','2020', '5313', '040301'}
bgColor= "#e7e7de"
entryBg = "#f8f1f1"
textColor = entryBg
textColor2 = '#00587a'
redTextColor = "#ed2a11"
entryTextColor = "#008891"
buttonColor1 = "#00587a"
buttonColor2 = "#008891"
testWithoutWO = False

#GENERATE NEW PASSWORD WINDOW
def passwordWindow():
    canContinue = False
    passwordWindow = tk.Tk()
    passwordWindow.geometry("230x70")
    passwordWindow.config(bg=bgColor)
    passwordWindow.title("Iniciar Sesión")
    passwordLabel = tk.Label(passwordWindow, text="Ingrese la contraseña")
    passwordLabel.config(font=('ARIAL', 13, 'bold'), fg="#00587a", bg=bgColor)
    passwordEntry = tk.Entry(passwordWindow, show="*")
    passwordEntry.config(font=('ARIAL', 13), fg=entryTextColor, bg=entryBg, relief="groove", borderwidth="2")
    passwordWindow.attributes("-topmost", True)
    passwordWindow.focus_force()

    #ENTER EVENT ACTION
    def enterEvent(event):
        if passwordEntry.get() in guiPasswords:
            passwordWindow.destroy()
            changeModel()

        else:
            pag.alert("Contraseña Incorrecta")
            passwordWindow.destroy()

        return canContinue;

    #KILL PASSWORD WINDOW
    def endProgram():
        passwordWindow.destroy()

    #DEFINE ENTER EVENT
    passwordWindow.bind('<Return>', enterEvent)

    #PACK LABELS, ENTRIES AND BUTTONS
    passwordLabel.pack()
    passwordEntry.pack()
    passwordWindow.focus()
    passwordEntry.focus()
    passwordWindow.protocol("WM_DELETE_WINDOW", endProgram)

    #ADD WIDGET TO MAINLOOP
    passwordWindow.mainloop()

    return keepActualModel

def contentionPasswordWindow():
    def endProgram():
        exit()
    passwordWindow = tk.Tk()
    passwordWindow.geometry("460x140")
    passwordWindow.config(bg=bgColor)
    passwordWindow.title("Iniciar Sesión")
    passwordLabel = tk.Label(passwordWindow, text="Ingrese la contraseña")
    passwordLabel.config(font=('ARIAL', 20, 'bold'), fg="#00587a", bg=bgColor)
    passwordEntry = tk.Entry(passwordWindow, show="*")
    passwordEntry.config(font=('ARIAL', 20), fg=entryTextColor, bg=entryBg, relief="groove", borderwidth="2")
    passwordWindow.protocol("WM_DELETE_WINDOW", endProgram)

    #ENTER EVENT ACTION
    def enterEvent(event):
        if passwordEntry.get() in guiPasswords:
            passwordWindow.destroy()

        else:
            pag.alert("Contraseña Incorrecta")
            passwordWindow.destroy()
            contentionWindow()


    #KILL PASSWORD WINDOW
    def endProgram():
        passwordWindow.destroy()

    #DEFINE ENTER EVENT
    passwordWindow.bind('<Return>', enterEvent)

    #PACK LABELS, ENTRIES AND BUTTONS
    passwordLabel.pack(pady=(20,0))
    passwordEntry.pack()
    passwordWindow.focus()
    passwordEntry.focus()
    passwordWindow.protocol("WM_DELETE_WINDOW", endProgram)

    #ADD WIDGET TO MAINLOOP
    passwordWindow.mainloop()

    return



def scanProduct():


    def testWithoutMes():
        global testWithoutWO
        testWithoutWO = True
        print(testWithoutWO)
        root.destroy()

    #CREATING WIDGET WINDOW
    print("Ejecutando scan product")
    global root
    root = tk.Tk()
    root.title("ATS Bot v4.0")
    root.config(bg=bgColor)
    root.iconbitmap("bot.ico")

    # CREATING TEXT VARIABLE FOR SERIAL NUMBER ENTRY
    global product
    product = tk.StringVar()

   ##########################   DEFINING LABELS, BUTTONS AND TEXTBOX    ##################################################

    #LABEL "ESCANEE EL NUMERO DE SERIE"
    label = tk.Label(root, text="Escaneé el número de serie:")
    label.config(font=('Franklin Gothic Medium', '40'), fg=textColor2, bg=bgColor)

    #CREATING AND SETTING UP TEXT BOX
    textBox = tk.Entry(root, textvariable=product, width=20)
    textBox.config(font=('Arial', 40), bd=4, bg=entryBg, fg="#008891")

    #GET THE SAVED MODEL FROM THE DB
    actualModel = hostDB.getModelFromDB()

    #CREATE, SET AND CONFIGURE MODEL LABEL
    modelLabel = tk.Label(root, text="Modelo actual: "+str(actualModel), borderwidth=1, relief="solid")
    modelLabel.config(font=('Franklin Gothic Medium', 20), fg="#008891", bg="#e7e7de", highlightbackground="#008891")

    #CREATE AND CONFIGURE "CHANGE MODEL" BUTTON
    changeModelBtn = tk.Button(root, text="CAMBIAR MODELO", command=passwordWindow)
    changeModelBtn.config(font=('Franklin Gothic Medium',13),fg=textColor, relief="groove", bg=buttonColor1)

    #CREATE AND CONFIGURE "TEST WITHOUT W/O"
    testWithoutWOBtn = tk.Button(root, text="PROBAR SIN W/O", command=testWithoutMes)
    testWithoutWOBtn.config(font=('Franklin Gothic Medium',14, "bold"), fg=textColor, relief="raised", bg=buttonColor2)

    #ENTER EVENT ACTION
    def enterEvent(event):
        global workOrder
        workOrder = tk.StringVar()
        x = re.search("[0-9]{4}(m|M){2}[0-9]{6}", product.get())
        if x:
            workOrder.set(product.get())
            root.destroy()
        else:
            pag.alert(title="ERROR", text="Introduzca una W/O valida.\nEj: 2045MM001234")
            textBox.delete('0', 'end')



    #KILL MODEL SELECTION WINDOW
    def endProgram():
        exit()



    #DEFINE "ENTER" KEY PRESS ACTION FOR THE ENTRY TEXTBOX
    root.bind('<Return>', enterEvent)

    ########################    PACK ALL THE COMPONENTS INTO THE WIDGETS    ##############
    label.grid(column=0, row=1, columnspan=2, padx=(20))
    textBox.grid(column=0, row=2, ipadx=20, columnspan=2, padx=(20), pady=(0,20))


    #############   IF ATS1, THEN ALLOW MANUALLY  MODEL SELECTION, ELSE DON'T PACK MANUALLY SELECT BUTTON###
    if AtsModel():
        label.grid(column=0, row=1, columnspan=2)
        textBox.grid(column=0, row=2, ipadx=20, columnspan=2, padx=(20))
        modelLabel.grid(column=1, row=3, ipady=5, pady=10, ipadx=15)
        testWithoutWOBtn.grid(column=3, row=2, ipady=14, padx=(0,20), pady=(0,20))
        #emptyLabel = tk.Label(root, text=" ").pack()
        changeModelBtn.grid(column=0, row=3, ipady=5, pady=10)




    #FOCUS TEXTBOX
    textBox.focus()

    #SELECT "X" BUTTON ACTION
    root.protocol("WM_DELETE_WINDOW", endProgram)
    root.mainloop()

#FUNCTION TO CREATE A NEW MODEL CHANGE WINDOW
def changeModel():
    #CREATING MAIN WINDOW
    comboValues = modelsDB.getModelsList()
    modelWindow = tk.Tk()
    modelWindow.config(bg = bgColor)
    modelWindow.geometry("400x150")
    ## CREATING LABEL AND COMBOBOX
    modelWindow.title("ATS Bot - Cambio de modelo")
    label = tk.Label(modelWindow, text="Seleccione el modelo:")
    label.config(font=('Franklin Gothic Medium', '25', "bold"), fg=textColor2, bg=bgColor)
    combobox = ttk.Combobox(modelWindow, values=comboValues, state="readonly",font=("Helvetica",20))
    modelWindow.option_add('*TCombobox*Listbox.font', ('Arial', '20'))

    def saveChangesFunction():
        model = combobox.get()
        print("File to be saved: "+model)
        modelFamily = model[0:3]
        extraLoadStringTitle = "E INSTALAR CARGAS 63108A"
        extraLoadStringText = ""
        print("Family to be saved corresponds to "+ modelFamily)
        if modelFamily == "ESD":
            pag.alert(title="CONECTAR TRANSFORMADOR",
                      text="Este modelo requiere el uso del Transformador,\n"
                      "conéctelo y presione OK para continuar")
        else:
            pag.alert(title="DESCONECTAR TRANSFORMADOR",
                      text="Este modelo NO requiere transformador, verifique que esté desconectado\n"
                      "y pulse OK para continuar")

        hostDB.writeModelInDB(model)
        print("Driver model saved")
        modelWindow.destroy()
        root.destroy()
        time.sleep(1)
        scanProduct()



    ## CREATING BUTTON
    saveChanges = tk.Button(modelWindow, text="Guardar Cambios", command=saveChangesFunction)
    saveChanges.config(font=('Franklin Gothic Medium',12, "bold"), relief='raised', fg=textColor, bg=buttonColor2, borderwidth="3")
    emptyLabel = tk.Label(modelWindow, text=" ")
    emptyLabel.config(bg = bgColor)
    label.pack()
    combobox.pack()
    emptyLabel.pack()
    saveChanges.pack()
    modelWindow.mainloop()


def getModelFromDB():
    if hostDB.getModelFromDB() is not None:
        model = hostDB.getModelFromDB()
        model = eval(model.replace('-', ''))
        return model
    else:
        pag.alert(title="Error", text='Ocurrio un error, solicite la presencia del tecnico de pruebas\n\n'
                  'Error: Model not found in DB')
        exit()


def mes():
    ##OPEN MES
    showDesktop()
    findAndClick(mesIconPic, 5, 0.8, True)
    findAndClick(mesLoginBtnPic, 10, 0.9, False)
    findAndClick(mesSideMenuBtnPic,10, 0.9,False)
    findAndClick(startWorkingSideMenuPic,10, 0.9,False)
    time.sleep(0.2)
    pag.press('tab')
    ## PASTE AND ENTER WO
    pag.write(workOrder.get())
    pag.press('enter')
    findAndClick(blueOKbtnPic,4, 0.9,False)
    time.sleep(0.2)
    pag.press('enter')

    #DEFINE GLOBAL VARIABLE TO STORE MODEL
    global model

    #IF ATS2, THEN PROCEED TO OBTAIN MODEL FROM PROCESS SCAN SEARCH TAB
    if AtsModel() is False:
        ##LOOK FOR PROCESS SCAN SEARCH
        findAndClick(processScanSearchPic, 5, 0.9, False)
        findAndClick(processScanSearchTextBoxPic, 5, 0.9, False)
        time.sleep(0.2)

        ##ENTER WO IN PROCESS SCAN SEARCH
        pag.write(workOrder.get())
        findAndClick(mesSearchBtnPic, 5, 0.9, False)
        time.sleep(0.5)
        pag.press('tab', presses=5)
        time.sleep(0.2)
        pag.keyDown('ctrlleft')
        pag.press('c')
        pag.keyUp('ctrlleft')

        ##SET MODEL INTO VARIABLE
        model = pyperclip.paste()
        model = eval(model.replace('-',''))
        modelFamily = model
        global previousModel
        previousModel = hostDB.getModelFromDB()
        global actualModel
        actualModel = modelFamily.model
        print("ACTUAL MODEL IS : "+actualModel)
        print("PREVIOUS MODEL IS : "+ previousModel)
        if actualModel == previousModel:
            print("Same models, no problem")
        else:
            if contentionWindow() is True:
                    hostDB.writeModelInDB(actualModel)
            else:
                main()

        showDesktop()
        if modelFamily.model[0:3] == "ESD":
            pag.alert(title="CONECTAR TRANSFORMADOR",
                      text="Este modelo requiere el uso del Transformador,\n"
                      "conéctelo y presione OK para continuar")
        else:
            pag.alert(title="DESCONECTAR TRANSFORMADOR",
                      text="Este modelo NO requiere transformador, verifique que esté desconectado\n"
                      "y pulse OK para continuar")
        return model
    else:
        return getModelFromDB()

def contentionWindow():
    def endProgram():
        killTasks()
        exit()

    global keepActualModel
    global actualModel
    global previousModel
    contentionWindow = tk.Tk()
    contentionWindow.title("LOS MODELOS SON DISTINTOS")
    contentionWindow.config(bg=bgColor)
    contentionWindow.state("zoomed")
    #contentionWindow.attributes("-fullscreen",True)
    contentionWindow.protocol("WM_DELETE_WINDOW", endProgram)

    def setActualModel():
         print("Arrived here")
         global keepActualModel
         keepActualModel = True
         contentionWindow.destroy()
         showDesktop()
         contentionPasswordWindow()
         print("After password dialog")



    def setPreviousModel():
        global keepActualModel
        keepActualModel = False
        contentionWindow.destroy()

    alertLabel = tk.Label(contentionWindow, text="ALERTA")
    alertLabel.config(font=("TAHOMA", 70), fg=redTextColor, bg=bgColor)

    mainTitle = tk.Label(contentionWindow, text="MODELOS DISTINTOS")
    mainTitle.config(font=("TAHOMA",60), fg=textColor2, bg=bgColor)

    textForPreviousModel = tk.Label(contentionWindow, text="El modelo que estaba cargado es el ")
    textForPreviousModel.config(font=("ARIAL",35), fg=textColor2, bg=bgColor)

    previousModelLabel = tk.Label(contentionWindow, text=previousModel)
    previousModelLabel.config(font=("ARIAL",35, 'bold'), fg=redTextColor, bg=bgColor)

    textForActualModel= tk.Label(contentionWindow, text="La pieza actual corresponde al modelo ")
    textForActualModel.config(font=("ARIAL", 35), fg=textColor2, bg=bgColor)

    actualModelLabel = tk.Label(contentionWindow, text=actualModel)
    actualModelLabel.config(font=("ARIAL", 35, 'bold'), fg=redTextColor, bg=bgColor)

    questionLabel = tk.Label(contentionWindow, text="¿Desea realizar el cambio de modelo?")
    questionLabel.config(font=("ARIAL", 35, 'bold'), fg=textColor2, anchor="center", bg=bgColor)

    continueButton = tk.Button(text="Continuar con el modelo\n"+previousModel, command=setPreviousModel)
    continueButton.config(font=('ARIAL', 20, 'bold'), fg=textColor, relief="groove", bg=buttonColor1)

    changeModelButton = tk.Button(text="Cambiar al modelo\n" + actualModel, command=setActualModel)
    changeModelButton.config(font=('ARIAL', 20, 'bold'), fg=textColor, relief="groove", bg=buttonColor1)





    alertLabel.grid(column=0, row=0, columnspan=2, pady=(20, 5))
    mainTitle.grid(column=0, row=1, columnspan=2, pady=(5, 30))
    textForPreviousModel.grid(column=0, row=2, sticky="E")
    previousModelLabel.grid(column=1, row=2, padx=(0,50), sticky="W")
    textForActualModel.grid(column=0, row=3, padx=(50, 0), sticky="E")
    actualModelLabel.grid(column=1, row=3, padx=(0,50), sticky="W")
    questionLabel.grid(column=0, row=4, columnspan=2, pady=(0,100))
    continueButton.grid(column=0, row=5, sticky="W", padx=(100,0), pady=(0,50))
    changeModelButton.grid(column=1, row=5, sticky="E", padx=(0,100), pady=(0,50), ipadx=45)
    contentionWindow.mainloop()

    return keepActualModel


def ats():
    # Open ATS
    findAndClick(atsShortcutPic,10, 0.90, True)
    time.sleep(0.2)
    #os.startfile("D:/ATS4/ATS For Mexico.exe")

    #findAndClick(runBtnPic, 5, 0.9, False)
    findAndClick(settingsBtnPic, 45, 0.9, False)
    if findAndBool(barcodeLabelPic, 10, 0.9):
        time.sleep(1)
        pag.press('tab', presses=2, interval=0.1)
        pag.press('enter')
    findAndClick(botTestFilesPic, 5, 0.95, True)
    findAndClick(ATS1FolderPic if AtsModel() else ATS2FolderPic, 5, 0.97, True)

    # FIRST TIME OPENING FILE
    pag.moveTo(40,40)
    while pag.locateCenterOnScreen(modelAtsFile, confidence=0.98) is None:
        print('Encontré el archivo')
        pag.scroll(-300)
    # LOAD FILE
    pag.doubleClick(pag.locateCenterOnScreen(modelAtsFile, confidence=0.98))
    time.sleep(0.3)
    while pag.locateCenterOnScreen(atsOpenBtnPic, confidence=0.95) is None:
        pag.scroll(-300)
    time.sleep(0.5)
    pag.click(pag.locateCenterOnScreen(atsOpenBtnPic))
    findAndClick(botTestFilesPic, 5, 0.95, True)
    findAndClick(ATS1FolderPic if AtsModel() else ATS2FolderPic, 5, 0.97, True)


    # SECOND TIME OPENING FILE
    pag.moveTo(40,40)
    while pag.locateCenterOnScreen(modelAtsFile, confidence=0.98) is None:
        pag.scroll(-300)
    pag.doubleClick(pag.locateCenterOnScreen(modelAtsFile, confidence=0.98))
    time.sleep(0.3)
    # FINISHED LOADING FILE

    # NEXT COMES CUSTOM MODEL SETTINGS
    print('before custom model settings')
    setSettings(model.writeCurrent, model.dwSwitch)
    print('after custom model settings')

    ### VALIDATE EVERYTHINGS OK
    if findAndBool(inventronicsLogoPic, 5, 0.95):
      pag.alert(title="ATS BOT",text='¡Configuración Exitosa! Puede comenza a probar.')
      exit()

def showDesktop():
    # SHOW DESKTOP
    time.sleep(0.2)
    pag.hotkey("win","d")


# INITIALIZING REQUIRED FUNCTIONS
def main():
    global model
    killTasks()
    scanProduct()
    if testWithoutWO is False:
        model = mes()
    else:
        model = getModelFromDB()
    global modelAtsFile
    modelAtsFile = model.ssAts1 if AtsModel() else model.ssAts2
    print("Model ATS file is "+modelAtsFile)
    showDesktop()
    FrameCurrent.openVisaIC(model.getCurrent(), model.getDWSwitch())
    ats()

main()


















