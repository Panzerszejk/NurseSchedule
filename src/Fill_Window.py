import tkinter as tk
from tkinter import *
from .Schedule import Schedule
from .Generator import Generator
from .ScheduleHandler import ScheduleHandler


class Fill_Window:
    def __init__(self,ward,root,frame):

        frame.destroy()

        sched = Schedule()
        gen = Generator()
        sched = gen.generate(ward)

        def fun(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=970,height=root.winfo_height()-200)

        na_dni = tk.Frame(root)
        na_dni.place(x=100,y=100)
        canvas = Canvas(na_dni)
        frame = Frame(canvas)
        scrollbar = Scrollbar(na_dni, orient=VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",fun)

        _dni = ["Poniedzialek", "Wtorek", "Sroda", "Czwartek", "Piatek", "Sobota", "Niedziela"]
        for x in range(0,35):
            dni = tk.Label(frame, text=_dni[x%7])
            dni.grid(row=x,column=0, ipadx=40, sticky='e')

        # Kod do testowania

        for x in range(0,35):
            for i in range(0,16):
                lbl = tk.Label(frame,relief='solid', bd=1)
                lbl.grid(row=x,column=i+1,ipadx=18)
                if str(ScheduleHandler.imported.importedWeek[x][i]) == "1" or str(ScheduleHandler.imported.importedWeek[x][i]) == "E":
                    lbl.configure(text="E")
                elif str(ScheduleHandler.imported.importedWeek[x][i]) == "2" or str(ScheduleHandler.imported.importedWeek[x][i]) == "D":
                    lbl.configure(text="D")
                elif str(ScheduleHandler.imported.importedWeek[x][i]) == "3" or str(ScheduleHandler.imported.importedWeek[x][i]) == "L":
                    lbl.configure(text="L")
                elif str(ScheduleHandler.imported.importedWeek[x][i]) == "4" or str(ScheduleHandler.imported.importedWeek[x][i]) == "N":
                    lbl.configure(text="N")
                elif str(ScheduleHandler.imported.importedWeek[x][i]) == "5" or str(ScheduleHandler.imported.importedWeek[x][i]) == "-":
                    lbl.configure(text="-")

"""
        for x in range(0,35):
            for i in range(0,16):
                lbl = tk.Label(frame,relief='solid', bd=1)
                lbl.grid(row=x,column=i+1,ipadx=18)
                
                if str(sched.scheduleList[x][i]) == "1":
                    lbl.configure(text="E")
                elif str(sched.scheduleList[x][i]) == "2":
                    lbl.configure(text="D")
                elif str(sched.scheduleList[x][i]) == "3":
                    lbl.configure(text="L")
                elif str(sched.scheduleList[x][i]) == "4":
                    lbl.configure(text="N")
                elif str(sched.scheduleList[x][i]) == "5":
                    lbl.configure(text="-")"""