from Tkinter import *
import Tkinter as tk
import autocomplete

#mEoWZw2C-FAAAAAAAAAAFSzkYI_I1DEDqw1fy-aHYy8zAB_OlahoT5p__XBoO8ps

#creates the patient select splash screen
def patientSelect():
    login = Tk()
    login.geometry("300x200")
    login.title("LOGIN to IHEARDC")
        
    def closeWindow():
        login.destroy()

    label_1 = Label(login, text="Patient ID: ")

    variable = StringVar(login)
    variable.set("Select Patient ID")
    label_1.pack()
    
    w = OptionMenu(login,variable, "00000000003Boa03","00000000433osu01", "00000000212agy02", "00000000311fri11")
    w.pack()
    #saves patient readings into a text file that coincides with thier patientID
    def savePID():
        global datafile
        
        if variable.get() == "00000000003Boa03":
            patientdata = open("00000000003Boa03.txt", "w+")
            datafile= "1"
        elif variable.get() == "00000000433osu01":
            patientdata = open("00000000433osu01.txt", "w+")
            datafile = "2"
        elif variable.get() == "00000000212agy02":
            patientdata = open("00000000212agy02.txt", "w+")
            datafile="3"
        elif variable.get() == "00000000311fri11":
            patientdata = open("00000000311fri11.txt", "w+")
            datafile="4"
        patientinput = variable.get()
        #patientdata.write("Patient ID: " + patientinput + "\n")
        patientdata.close()

        

    c = Button(login,text="Click to proceed \n with Selected Patient")
    c.pack()
    c.configure(state=ACTIVE)
    #c.configure(command = savePID)
    c.configure(command = lambda:[savePID(),closeWindow()])

    login.mainloop()
#reads in the patient file so that it can be output to the screen
def readFile():
    
    if datafile == "1":
        patientFile= open("00000000003Boa03.txt","r")
    elif datafile == "2":
        patientFile = open("00000000433osu01.txt", "r")
    elif datafile == "3":
        patientFile = open ("00000000212agy02.txt", "r")
    elif datafile == "4":
        patientFile = open("00000000311fri11.txt", "r")

    return patientFile
#this function will open the file and allow it to be written to.
def openAppendFile():
    
    if datafile == "1":
        patientFile= open("00000000003Boa03.txt","a+")
    elif datafile == "2":
        patientFile = open("00000000433osu01.txt", "a+")
    elif datafile == "3":
        patientFile = open ("00000000212agy02.txt", "a+")
    elif datafile == "4":
        patientFile = open("00000000311fri11.txt", "a+")

    return patientFile

#this function closes the patient info window.
def show_patientdata():
    def closeWindow():
        patientInfo.destroy()

    patientFile= readFile()
    
    #creates gui window
    patientInfo = tk.Toplevel(myGUI)
    patientInfo.geometry("600x400")

#all below fucntions are building the GUI for patientInfo
    topFrame= Frame(patientInfo)
    topFrame.pack()

    pInfoFrame = Frame(patientInfo)
    pInfoFrame.pack(fill="both", expand=True)

    lowFrame = Frame(patientInfo)
    lowFrame.pack()

    label= Label(topFrame)
    label.pack()
    label.configure(text="Patient Data")

    patientInput = patientFile.read()
    
    textOutput = Text(pInfoFrame, wrap=NONE, height = 17, width = 70, borderwidth=0)
    textOutput.insert('1.0', patientInput)
    vscroll = Scrollbar(pInfoFrame,orient=VERTICAL, command= textOutput.yview)
    textOutput['yscroll']=vscroll.set
    vscroll.pack(side="right", fill="y")
    textOutput.pack(side="left", fill="both", expand=True)

    b=Button(lowFrame)
    b.pack()
    b.configure(text="Close Window", command = closeWindow)

def create_ekg():

    def closeWindow():
        ekgData.destroy()

    def saveData():
        patientFile = openAppendFile()
        dataEntry = dataInput.get()
        dataType = sensorType
        patientFile.write( dataType + dataEntry + "\n")

    def clearData():
        ekgSensorFile = open("ecgvalue.txt","w")
        ekgSensorFile.write()
    
    ekgSensorFile = open("ecgvalue.txt","r")
    sensorType = "EKG: "
    
    ekgData = tk.Toplevel(myGUI)
    ekgData.geometry("600x400")
    
    ekgLabelFrame = Frame(ekgData)
    ekgLabelFrame.pack()
    
    ekgLabel = Label(ekgLabelFrame)
    ekgLabel.pack()
    ekgLabel.configure(text= '''EKG SENSOR DATA''')

    ekgFrame = Frame(ekgData)
    ekgFrame.pack(fill="both", expand=True)
    ekgFrame.configure(relief=GROOVE, borderwidth="2", width=595)
    
    ekgInput = ekgSensorFile.read()
    
    textOutput = Text(ekgFrame, wrap=NONE, height = 17, width = 70, borderwidth=0)
    textOutput.insert('1.0', ekgInput)
    vscroll = Scrollbar(ekgFrame,orient=VERTICAL, command= textOutput.yview)
    textOutput['yscroll']=vscroll.set
    vscroll.pack(side="right", fill="y")
    textOutput.pack(side="left", fill="both", expand=True)

    dataLabel= Label(ekgData)
    dataLabel.pack(side=TOP)
    dataLabel.configure(text='''Please enter reading below(type or hightlight & copy using ctrl+c) then click save''')

    dataEntryFrame = Frame(ekgData)
    dataEntryFrame.pack(fill=X)
    
    dataInput = Entry(dataEntryFrame)
    dataInput.pack(fill=X)

    #clear = Button(ekgData)
    #clear.pack(side=BOTTOM)
    #clear.configure(text='''Clear all readings''', command=clearData)

    ekgSave = Button(ekgData)
    ekgSave.pack(side=BOTTOM)
    ekgSave.configure(activebackground="#d9d9d9")
    ekgSave.configure(state=ACTIVE)
    ekgSave.configure(text='''Save EKG Reading''', command = lambda:[saveData(),closeWindow()])

def create_gsr():

    def closeWindow():
        gsrData.destroy()

    def saveData():
        patientdata = openAppendFile()
        dataEntry = dataInput.get()
        dataType = sensorType
        patientdata.write( dataType + dataEntry + "\n")

    def clearData():
        gsrFile = open("gsr.txt","w")
        gsrFile.write()
        
        
    gsrSensorFile = open("gsr.txt","r")
    sensorType = "Galvanic Skin Response: "
                      
    gsrData = tk.Toplevel(myGUI)
    gsrData.geometry("800x600")

    gsrLabelFrame = Frame(gsrData)
    gsrLabelFrame.pack()

    gsrLabel = Label(gsrLabelFrame)
    gsrLabel.pack()
    gsrLabel.configure(text= '''GSR SENSOR DATA''')
    
    gsrFrame = Frame(gsrData)
    gsrFrame.pack(fill="both", expand=True)
    gsrFrame.configure(relief=GROOVE, borderwidth="2", width=595)


    gsrInput = gsrSensorFile.read()
    
    textOutput = Text(gsrFrame, wrap=NONE, height = 17, width = 70, borderwidth=0)
    textOutput.insert('1.0', gsrInput)
    vscroll = Scrollbar(gsrFrame,orient=VERTICAL, command= textOutput.yview)
    textOutput['yscroll']=vscroll.set
    vscroll.pack(side="right", fill="y")
    textOutput.pack(side="left", fill="both", expand=True)
    
    dataLabel= Label(gsrData)
    dataLabel.pack(side=TOP)
    dataLabel.configure(text='''Please enter reading below(type or hightlight & copy using ctrl+c) then click save''')
                        
    dataEntryFrame = Frame(gsrData)
    dataEntryFrame.pack(fill=X)

    dataInput = Entry(dataEntryFrame)
    dataInput.pack(fill=X)

    #clear = Button(gsrData)
    #clear.pack(side=BOTTOM)
    #clear.configure(text='''Clear all readings''', command=clearData)

    gsrSave = Button(gsrData)
    gsrSave.pack(side=BOTTOM)
    gsrSave.configure(activebackground="#d9d9d9")
    gsrSave.configure(state=ACTIVE)
    gsrSave.configure(text='''Save GSR Reading''', command =lambda:[saveData(),closeWindow()])

def create_bp():
    def closeWindow():
        bpData.destroy()
    
    def saveData():
        patientdata = openAppendFile()
        dataEntry = dataInput.get()
        dataType = sensorType
        patientdata.write( dataType + dataEntry + "\n")

    def clearData():
        bpFile = open("ecgvalue.txt","w")
        bpFile.write()
        
    bpSensorFile = open("bpvalue.txt","r") #need to change this to bloodpressure.txt when sensor available
    sensorType = "Blood Pressure: "

    bpData = tk.Toplevel(myGUI)
    bpData.geometry("800x600")

    bpLabelFrame = Frame(bpData)
    bpLabelFrame.pack()

    bpLabel = Label(bpLabelFrame)
    bpLabel.pack()
    bpLabel.configure(text= '''BLOOD PRESSURE DATA''')
    
    bpFrame = Frame(bpData)
    bpFrame.pack(fill="both",expand=True)
    bpFrame.configure(relief=GROOVE, borderwidth="2", width=595)

    bpInput = bpSensorFile.read()
    
    textOutput = Text(bpFrame, wrap=NONE, height = 17, width = 70, borderwidth=0)
    textOutput.insert('1.0', bpInput)
    vscroll = Scrollbar(bpFrame,orient=VERTICAL, command= textOutput.yview)
    textOutput['yscroll']=vscroll.set
    vscroll.pack(side="right", fill="y")
    textOutput.pack(side="left", fill="both", expand=True)

    dataLabel= Label(bpData)
    dataLabel.pack(side=TOP)
    dataLabel.configure(text='''Please enter reading below(type or hightlight & copy using ctrl+c) then click save''')

    dataEntryFrame = Frame(bpData)
    dataEntryFrame.pack(fill=X)

    dataInput = Entry(dataEntryFrame)
    dataInput.pack(fill=X)

    #clear = Button(bpData)
    #clear.pack(side=BOTTOM)
    #clear.configure(text='''Clear all readings''', command=clearData)
                 
    bpSave = Button(bpData)
    bpSave.pack(side=BOTTOM)
    bpSave.configure(activebackground="#d9d9d9")
    bpSave.configure(state=ACTIVE)
    bpSave.configure(text='''Save Blood Pressure Reading''')
    bpSave.configure(command=lambda:[saveData(),closeWindow()])

    
def create_spo2():

    def closeWindow():
        spo2Data.destroy()
    
    def saveData():
        patientdata = openAppendFile()
        dataEntry = dataInput.get()
        dataType = sensorType
        patientdata.write( dataType + dataEntry + "\n")

    def clearData():
        spo2File = open("ecgvalue.txt","w")
        spo2File.write()
        
    spo2SensorFile = open("temp.txt","r") #need to change when sensor is programmed
    sensorType = "Temperature: "
    
    spo2Data = tk.Toplevel(myGUI)
    spo2Data.geometry("800x600")

    spo2LabelFrame = Frame(spo2Data)
    spo2LabelFrame.pack()

    spo2Label = Label(spo2LabelFrame)
    spo2Label.pack()
    spo2Label.configure(text= '''Temperature Data''')
    
    spo2Frame = Frame(spo2Data)
    spo2Frame.pack(fill="both",expand=True)
    spo2Frame.configure(relief=GROOVE, borderwidth="2", width=595)

    spo2Input = spo2SensorFile.read()
    
    textOutput = Text(spo2Frame, wrap=NONE, height = 17, width = 70, borderwidth=0)
    textOutput.insert('1.0', spo2Input)
    vscroll = Scrollbar(spo2Frame,orient=VERTICAL, command= textOutput.yview)
    textOutput['yscroll']=vscroll.set
    vscroll.pack(side="right", fill="y")
    textOutput.pack(side="left", fill="both", expand=True)

    dataLabel= Label(spo2Data)
    dataLabel.pack(side=TOP)
    dataLabel.configure(text='''Please enter reading below(type or hightlight & copy using ctrl+c) then click save''')

    dataEntryFrame = Frame(spo2Data)
    dataEntryFrame.pack(fill=X)
                 
    dataInput = Entry(dataEntryFrame)
    dataInput.pack(side=TOP, fill =X)

    #clear = Button(spo2Data)
    #clear.pack(side=BOTTOM)
    #clear.configure(text='''Clear all readings''', command=clearData)

    spo2Save = Button(spo2Data)
    spo2Save.pack(side=BOTTOM)
    spo2Save.configure(activebackground="#d9d9d9")
    spo2Save.configure(state=ACTIVE)
    spo2Save.configure(text='''Save Temp Reading''', command = lambda:[saveData(), closeWindow()])
#autocomplete fucntion that was taken from online, used in the symtoms. 
class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):
        
        Entry.__init__(self, *args, **kwargs)
        self.lista = lista        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]
    
patientSelect()
#auto complete symptoms
snomed = ['Cracked Tooth(109747007)', 'Dental Abscess(299709002)', 'Gingivitis(66383009)','Cracked lips (248182008)', 'Lesion of Lip (301350008)', 'Black Hairy Tongue(81934005)', "Crohn's Disease of esophagus(235607002)", 'Alkaline reflux disease(1027000)','Acid reflux(698065002)']
#creation of main GUI
myGUI =Tk()
myGUI.geometry("1280x720")
myGUI.title("I HEAR DC")

topFrame = Frame(myGUI)
topFrame.pack(fill="both")

upperFrame = Frame(myGUI)
upperFrame.pack(side=TOP, fill="both", expand=True)
upperFrame.configure(relief=GROOVE)
upperFrame.configure(borderwidth="2")


bottomFrame = Frame(myGUI)
bottomFrame.pack(side=BOTTOM,fill="both")
bottomFrame.configure(relief=GROOVE)
bottomFrame.configure(borderwidth="2")

lowerFrame = Frame(myGUI)
lowerFrame.pack(side=BOTTOM,fill="both", expand=True)
lowerFrame.configure(relief=GROOVE)
lowerFrame.configure(borderwidth="2")
#builds EKG button
ekg = Button(upperFrame)
ekg.pack(side=LEFT,fill="both", expand=True)
ekg.configure(activebackground="#d9d9d9")
ekg.configure(background="#d9010e")
ekg.configure(state=ACTIVE)
ekg.configure(text='''EKG''')
ekg.configure(command = create_ekg)
#builds SPO2 button
spo2 = Button(upperFrame)
spo2.pack(side=LEFT,fill="both", expand=True)
spo2.configure(activebackground="#d9d9d9")
spo2.configure(background="#f8ffff")
spo2.configure(overrelief="raised")
spo2.configure(text='''Temp''')
spo2.configure(command=create_spo2)
#builds blood pressure button
bp = Button(lowerFrame)
bp.pack(side=LEFT,fill="both", expand=True)
bp.configure(activebackground="#d9d9d9")
bp.configure(background="#ffffff")
bp.configure(text='''Blood \nPressure''')
bp.configure(command=create_bp)
#builds gsr button
gsr = Button(lowerFrame)
gsr.pack(side=LEFT,fill="both", expand = True)
gsr.configure(activebackground="#d9d9d9")
gsr.configure(background="#d9101e")
gsr.configure(text='''Galvanic \n Skin \n Response''')
gsr.configure(command=create_gsr)
#below function saves symtoms entered
def save():
    patientdata = openAppendFile()
    input = sEntry.get()
    patientdata.write("Symptoms: " + input + "\n")
    patientdata.close()

symptom = Label(topFrame)
symptom.pack()
symptom.configure(text = '''Please enter Symptoms below: ''')

sEntry = AutocompleteEntry(snomed, topFrame)
sEntry.pack(fill=X, expand = True)

sButton = Button(topFrame)
sButton.pack()
sButton.configure(state=ACTIVE)
sButton.configure(text = '''Save Symptoms to File''')
sButton.configure(command = save)

returnButton = Button(bottomFrame)
returnButton.pack(side=BOTTOM)
returnButton.configure(text = '''Return to \n Patient Select''',command=patientSelect)

viewButton = Button(bottomFrame)
viewButton.pack(side=BOTTOM)
viewButton.configure(text = '''View Patient File''', command=show_patientdata)

myGUI.mainloop()
