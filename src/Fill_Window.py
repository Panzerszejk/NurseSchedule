import tkinter as tk
from tkinter import ttk
from tkinter import *
from .LogsWindow import LogsWindow
from src.ConstraintChecker import ConstraintChecker
from .ScheduleHandler import ScheduleHandler
from .Generator import Generator
#from numpy import *

class Fill_Window:
    def __init__(self,ward,root,frame):

        frame.destroy()

        self.lista_do_decodowania = []
        self.lista_na_elementy = []
        gen = Generator()
        sched = gen.generate(ward)
        print(sched.scheduleList)
        def fun(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=700,height=root.winfo_height()-200)
        na_dni = tk.Frame(root)
        if root.winfo_width()>1920:
            na_dni.place(x = root.winfo_width() / 2 - 700 / 2, y = 100)
        else:
            na_dni.place(x=root.winfo_width()/2-700*2/3,y=100)
        canvas = Canvas(na_dni)
        frame = Frame(canvas)
        scrollbar = Scrollbar(na_dni, orient=VERTICAL, command=canvas.yview)
        if root.winfo_height()<1080:
            canvas.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",fun)

        _dni = ["Poniedzialek", "Wtorek", "Sroda", "Czwartek", "Piatek", "Sobota", "Niedziela"]
        for x in range(0,35):
            dni = tk.Label(frame, text=_dni[x%7])
            dni.grid(row=x,column=0, ipadx=40, sticky='e')


        for x in range(0,35):
            for i in range(0,16):
                lbl = tk.Label(frame,relief='solid', bd=1, font=("Consolas"))
                lbl.grid(row=x,column=i+1,ipadx=10)
                if str(sched.scheduleList[x][i]) == "E":
                    self.lista_na_elementy.append('E')
                    lbl.configure(text="E")
                elif str(sched.scheduleList[x][i]) == "D":
                    self.lista_na_elementy.append('D')
                    lbl.configure(text="D")
                elif str(sched.scheduleList[x][i]) == "L":
                    self.lista_na_elementy.append('L')
                    lbl.configure(text="L")
                elif str(sched.scheduleList[x][i]) == "N":
                    self.lista_na_elementy.append('N')
                    lbl.configure(text="N")
                elif str(sched.scheduleList[x][i]) == "-":
                    self.lista_na_elementy.append('-')
                    
                    lbl.configure(text="-")
            self.lista_do_decodowania.append(self.lista_na_elementy[:])
            self.lista_na_elementy.clear()


        def decoder(frame):
            frame.destroy()
            def fun( event ):
                canvas.configure(scrollregion = canvas.bbox("all"), width = 700, height = root.winfo_height() - 200)

            na_dni = tk.Frame(root)
            if root.winfo_width() > 1920:
                na_dni.place(x = root.winfo_width() / 2 - 700 / 2, y = 100)
            else:
                na_dni.place(x = root.winfo_width() / 2 - 700 * 2 / 3, y = 100)
            canvas = Canvas(na_dni)
            frame = Frame(canvas)
            scrollbar = Scrollbar(na_dni, orient = VERTICAL, command = canvas.yview)
            if root.winfo_height() < 1080:
                canvas.configure(yscrollcommand = scrollbar.set)
                scrollbar.pack(side = "right", fill = "y")
            canvas.pack(side = "left")
            canvas.create_window((0, 0), window = frame, anchor = 'nw')
            frame.bind("<Configure>", fun)

            _dni = ["Poniedzialek", "Wtorek", "Sroda", "Czwartek", "Piatek", "Sobota", "Niedziela"]
            for x in range(0, 35):
                dni = tk.Label(frame, text = _dni[x % 7])
                dni.grid(row = x, column = 0, ipadx = 40, sticky = 'e')


            for x in range(0, 35):
                for i in range(0, 16):
                    lbl = tk.Label(frame, relief = 'solid', bd = 1, font = ("Consolas"))
                    lbl.grid(row = x, column = i + 1, ipadx = 10)
                    if str(self.lista_do_decodowania[x][i]) == "E":
                        lbl.configure(text = "1")
                    elif str(self.lista_do_decodowania[x][i]) == "D":
                        lbl.configure(text = "2")
                    elif str(self.lista_do_decodowania[x][i]) == "L":
                        lbl.configure(text = "3")
                    elif str(self.lista_do_decodowania[x][i]) == "N":
                        lbl.configure(text = "4")
                    elif str(self.lista_do_decodowania[x][i]) == "-":
                        lbl.configure(text = "5")
                    elif str(self.lista_do_decodowania[x][i]) == "1":
                        lbl.configure(text = "E")
                    elif str(self.lista_do_decodowania[x][i]) == "2":
                        lbl.configure(text = "D")
                    elif str(self.lista_do_decodowania[x][i]) == "3":
                        lbl.configure(text = "L")
                    elif str(self.lista_do_decodowania[x][i]) == "4":
                        lbl.configure(text = "N")
                    elif str(self.lista_do_decodowania[x][i]) == "5":
                        lbl.configure(text = "-")


            for x in range(0,35):
                for y in range(0,16):
                    if self.lista_do_decodowania[x][y] == "E":
                        self.lista_do_decodowania[x][y] = "1"
                        continue
                    elif str(self.lista_do_decodowania[x][y]) == "D":
                        self.lista_do_decodowania[x][y] = "2"
                        continue
                    elif str(self.lista_do_decodowania[x][y]) == "L":
                        self.lista_do_decodowania[x][y] = "3"
                        continue
                    elif str(self.lista_do_decodowania[x][y]) == "N":
                        self.lista_do_decodowania[x][y] = "4"
                        continue
                    elif str(self.lista_do_decodowania[x][y]) == "-":
                        self.lista_do_decodowania[x][y] = "5"
                        continue
                    elif str(self.lista_do_decodowania[x][y]) == "1":
                        self.lista_do_decodowania[x][y] = "E"
                        continue
                    elif str(self.lista_do_decodowania[x][y]) == "2":
                        self.lista_do_decodowania[x][y] = "D"
                        continue
                    elif str(self.lista_do_decodowania[x][y]) == "3":
                        self.lista_do_decodowania[x][y] = "L"
                        continue
                    elif str(self.lista_do_decodowania[x][y]) == "4":
                        self.lista_do_decodowania[x][y] = "N"
                        continue
                    elif str(self.lista_do_decodowania[x][y]) == "5":
                        self.lista_do_decodowania[x][y] = "-"
                        continue


        decoderr = ttk.Button(root, text = "Decode", command = lambda: decoder(frame))
        if root.winfo_width() > 1900:
            decoderr.place(x = root.winfo_width() - 300, y = 240, width = 120, height = 50)
        else:
            decoderr.place(x = 1170, y = 240, width = 120, height = 50)

        constchecker = ConstraintChecker(ward,sched,ScheduleHandler.imported)
        constchecker.check()
        hardbreach = constchecker.checkHard('all')
        logs = tk.Button(root, text = "Constrains", command = lambda: LogsWindow(constchecker.infoTable,hardbreach))
        if root.winfo_width() > 1900:
            logs.place(x = root.winfo_width() - 300, y = 310, width = 120, height = 50)
        else:
            logs.place(x = 1170, y = 310, width = 120, height = 50)

