from tkinter import *
import tkinter as tk
from .Ward import Ward
from .Schedule import Schedule
from .ScheduleHandler import ScheduleHandler
from .Week import Week
from .Generator import Generator
from .Fill_Window import Fill_Window

class View:
    ward = Ward()
    sched = Schedule().scheduleList

    @staticmethod
    def import_schedule(sched):
        View.sched=sched

    @staticmethod
    def import_ward(ward):
        View.ward=ward

    def __init__(self):

        root = tk.Tk()
        root.attributes("-fullscreen", True)
        root.update()

        wyjdz = tk.Button(root, text = "X", command = root.destroy,
            highlightcolor = 'red', activebackground = 'red')
        wyjdz.place(x = root.winfo_width() - 35, y = 0,
            width = 35, height = 20)

        import_week = tk.Button(root, text = "Import week", command = lambda: ScheduleHandler.importer("week"))
        import_week.place(x = 1170, y = 100, width = 120, height = 50)

        export_schedule = tk.Button(root, text = "Export", command = lambda: ScheduleHandler.export(Week().weekList))
        export_schedule.place(x = 1170, y = 170, width = 120, height = 50)

        clear = tk.Button(root, text = "Wyczyść", command = lambda: ScheduleHandler.clear())
        clear.place(x = 1170, y = 410, width = 120, height = 50)

        y=0
        for x in range(0,16):
            nazwy = View.ward.print_initials(x)
            nazwa = tk.Label(root,text=nazwy, bd=1, relief=SOLID, font=("Consolas"))
            nazwa.place(x=255+y,y=50,width=30,height=20)
            y=y+33

        def fun(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=700,height=root.winfo_height()-200)

        na_dni = tk.Frame(root)
        na_dni.place(x=100,y=100)
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

        generate = tk.Button(root, text = "Generate", command = lambda: Fill_Window(View.ward,root,frame))
        # generate = tk.Button(root, text = "Generate", command = lambda: ScheduleHandler.generate(ward))
        generate.place(x = 1170, y = 340, width = 120, height = 50)

        root.mainloop()