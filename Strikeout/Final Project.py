from tkinter import *
import sys
import time
from threading import Timer

level = 0
combo = ""
comboLvl = 0
score = 0
moveCap = 10
moves = 0

class StrikeLaunch(Tk):

    def __init__(self,*args,**kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartGUI,GameUI,WinScreen,LoseScreen):
            page_name = F.__name__
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartGUI)

    def show_frame(self, cont):
        #GameUI.points['text'] = "Score Req: " + str(score)
        frame = self.frames[cont]
        frame.tkraise()
    def update(self, cont):
        GameUI.points['text'] = "Score Req: " + str(score)
        GameUI.movesUp['text'] = "Moves: " + str(moves)
        GameUI.movCap['text'] = "Move Cap: " + str(moveCap)
        
# start GUI
class StartGUI(Frame):
    # constructor
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.setupGUI()

    def setupGUI(self):

        for row in range(15):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(11):
            Grid.columnconfigure(self, col, weight=1)

        
        img = PhotoImage(file="images/icon.png")
        self.display = Label(self, image=img)
        self.display.image = img
        self.display.grid(row=1, column=0, columnspan=11, rowspan=2, sticky=N+S+E+W)


        StartGUI.entry = Label(self, text="Level:", font=("TexGyreAdventor", 40))
        StartGUI.entry.grid(row=3, column=5)

        StartGUI.enter = Entry(self)
        StartGUI.enter.bind("<Return>", self.process)
        StartGUI.enter.grid(row=4, column=5)
        StartGUI.enter.focus()

        img = PhotoImage(file="images/play.png")
        button = Button(self,image=img, borderwidth=1, highlightthickness=0, command=self.process2)
        button.image = img
        button.configure(height=15,width=200)
        button.grid(row=6, column=5, columnspan=1,rowspan=1, sticky=N+S+E+W)

        img = PhotoImage(file="images/exit.png")
        button = Button(self, image=img, borderwidth=1, highlightthickness=0, command=self.quit)
        button.image = img
        button.configure(height=15,width=200)
        button.grid(row=8, column=5, columnspan=1,rowspan=1, sticky=N+S+E+W)

    def process(self, event):
        global level
        level = int(StartGUI.enter.get())
        if(level>10 or level<1):
            StartGUI.entry['text'] = "Please select a level from 1-10:"
        else:
            StartGUI.entry['text'] = "Level: " + str(level) + " confirmed."
    def process2(self):
        global score
        global moveCap
        if(level<=10 and level>=1):
            if(level==1):
                score = 100
                moveCap = 20
            if(level==2):
                score = 200
                moveCap = 20
            if(level==3):
                score = 300
                moveCap = 20
            if(level==4):
                score = 420
                moveCap = 24
            if(level==5):
                score = 233
                moveCap = 20
            if(level==6):
                score = 69
                moveCap = 7
            if(level==7):
                score = 666
                moveCap = 20
            if(level==8):
                score = 42
                moveCap = 20
            if(level==9):
                score = 99
                moveCap = 20
            if(level==10):
                score==1000
                moveCap = 10
            self.controller.update(GameUI)
            self.controller.show_frame(GameUI)


    # ends game
    def quit(self):
        window.destroy()
    

# game GUI

class GameUI(Frame):
    # constructor
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.setupGUI()

    def setupGUI(self):
        global score
        global moveCap
        global moves
        self.display = Label(self, text="", anchor=E,bg="white", height=1, font=("TexGyreAdventor", 18))
        self.display.place(x=390,y=45)

        for row in range(15):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(11):
            Grid.columnconfigure(self, col, weight=1)

        standImg = PhotoImage(file="images/standpic.png")
        self.character = Label(self, image=standImg)
        self.character.image = standImg
        self.character.place(x=1, y=5)
        
        img = PhotoImage(file="images/punch.png")
        button = Button(self,image=img,borderwidth=0,highlightthickness=0, command=lambda: self.process("punch"))
        button.image = img
        button.place(x=460, y=305)

        img = PhotoImage(file="images/kick.png")
        button = Button(self,image=img,borderwidth=0,highlightthickness=0, command=lambda: self.process("kick"))
        button.image = img
        button.place(x= 575, y=265)

        img = PhotoImage(file="images/shield.png")
        button = Button(self,image=img,borderwidth=0,highlightthickness=0, command=lambda: self.process("defend"))
        button.image = img
        button.place(x=690, y=225)

        GameUI.points = Label(self, text="Score Req: " + str(score))
        GameUI.points.place(x=600, y=20)

        GameUI.movCap = Label(self, text="Move Cap: " + str(moveCap))
        GameUI.movCap.place(x=500, y=20)

        GameUI.movesUp = Label(self, text="Moves: " + str(moves))
        GameUI.movesUp.place(x=400, y=20)


    # processes button presses
    def process(self, button):
        global score
        global comboLvl
        global combo
        global moves
        global moveCap
        global win
        standImg = PhotoImage(file="images/standpic.png")
        guardImg = PhotoImage(file="images/guardpic.png")
        punchImg = PhotoImage(file="images/punchpic.png")
        kickImg = PhotoImage(file="images/kickpic.png")
        if(button == "punch"):
            self.display["text"] = "PUNCH: 10 damage"
            comboLvl+=1
            combo+="1"
            moves+=1
            self.movesUp['text'] = "Moves: " + str(moves)
            self.movCap['text'] = "Move Cap: " + str(moveCap)
            if(comboLvl==3):
                self.ccccombo(combo)
            else:
                score-=10
                self.points['text'] = "Score Req: " + str(score)
            
            self.character.configure(image=punchImg)
            self.character.image = punchImg
            self.character.place(x=1, y=5)
                
        if(button == "kick"):
            self.display["text"] = "KICK: 10 damage"
            comboLvl+=1
            combo+="2"
            moves+=1
            self.movesUp['text'] = "Moves: " + str(moves)
            self.movCap['text'] = "Move Cap: " + str(moveCap)
            if(comboLvl==3):
                self.ccccombo(combo)
            else:
                score-=10
                self.points['text'] = "Score Req: " + str(score)

            self.character.configure(image=kickImg)
            self.character.image = kickImg
            self.character.place(x=1, y=5)
                
        if(button == "defend"):
            self.display["text"] = "BLOCK: combo cancled"
            comboLvl = 0
            combo=""
            moves+=1
            self.movesUp['text'] = "Moves: " + str(moves)
            self.movCap['text'] = "Move Cap: " + str(moveCap)
            self.points['text'] = "Score Req: " + str(score)

            self.character.configure(image=guardImg)
            self.character.image = guardImg
            self.character.place(x=1, y=5)
            
        if(moves>moveCap):
            self.controller.show_frame(LoseScreen)
        if(score<0):
            self.controller.show_frame(LoseScreen)
        if(score==0):
            win = True
            self.controller.show_frame(WinScreen)


    def ccccombo(self, ccombo):
        global comboLvl
        global score
        if(ccombo=="111"):
            score-=15
            self.display["text"] = "c-c-c-COMBO: 15 damage"
            self.points['text'] = "Score Req: " + str(score)
            comboLvl = 0
        elif(ccombo=="112"):
            score-=18
            self.display["text"] = "c-c-c-COMBO: 18 damage"
            self.points['text'] = "Score Req: " + str(score)
            comboLvl = 0
        elif(ccombo=="121"):
            score-=17
            self.display["text"] = "c-c-c-COMBO: 17 damage"
            self.points['text'] = "Score Req: " + str(score)
            comboLvl = 0
        elif(ccombo=="122"):
            score-=22
            self.display["text"] = "c-c-c-COMBO: 22 damage"
            self.points['text'] = "Score Req: " + str(score)
            comboLvl = 0
        elif(ccombo=="211"):
            score-=16
            self.display["text"] = "c-c-c-COMBO: 16 damage"
            self.points['text'] = "Score Req: " + str(score)
            comboLvl = 0
        elif(ccombo=="212"):
            score-=34
            self.display["text"] = "c-c-c-COMBO: 34 damage"
            self.points['text'] = "Score Req: " + str(score)
            comboLvl = 0
        elif(ccombo=="221"):
            score-=19
            self.display["text"] = "c-c-c-COMBO: 19 damage"
            self.points['text'] = "Score Req: " + str(score)
            comboLvl = 0
        elif(ccombo=="222"):
            score-=20
            self.display["text"] = "c-c-c-COMBO: 20 damage"
            self.points['text'] = "Score Req: " + str(score)
            comboLvl = 0
        global combo
        combo = ""


class WinScreen(Frame):
    # constructor
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.setupGUI()

    def setupGUI(self):

        for row in range(15):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(11):
            Grid.columnconfigure(self, col, weight=1)


   
        img = PhotoImage(file="images/strikeout.png")
        self.display = Label(self, image=img)
        self.display.image = img
        self.display.grid(row=1, column=0, columnspan=11, rowspan=2, sticky=N+S+E+W)

        img = PhotoImage(file="images/exit.png")
        button = Button(self, image=img, borderwidth=1, highlightthickness=0, command=self.quit)
        button.image = img
        button.configure(height=15,width=200)
        button.grid(row=8, column=5, columnspan=1,rowspan=1, sticky=N+S+E+W)


    # ends game
    def quit(self):
        global moves
        moves = 0
        self.controller.show_frame(StartGUI)

class LoseScreen(Frame):
    # constructor
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.setupGUI()

    def setupGUI(self):

        for row in range(15):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(11):
            Grid.columnconfigure(self, col, weight=1)


   
        img = PhotoImage(file="images/lose.png")
        self.display = Label(self, image=img)
        self.display.image = img
        self.display.grid(row=1, column=0, columnspan=11, rowspan=2, sticky=N+S+E+W)

        img = PhotoImage(file="images/exit.png")
        button = Button(self, image=img, borderwidth=1, highlightthickness=0, command=self.quit)
        button.image = img
        button.configure(height=15,width=200)
        button.grid(row=8, column=5, columnspan=1,rowspan=1, sticky=N+S+E+W)


    # ends game
    def quit(self):
        global moves
        moves = 0
        self.controller.show_frame(StartGUI)
window = StrikeLaunch()
window.title("Strikout Warrior!")
window.geometry("1024x600")
window.mainloop()
