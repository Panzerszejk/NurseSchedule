from tkinter import *
import tkinter as tk
from tkinter import ttk
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

        import_week = ttk.Button(root, text = "Import week", command = lambda: ScheduleHandler.importer("week"))
        if root.winfo_width()>1900:
            import_week.place(x = root.winfo_width() - 300, y = 100, width = 120, height = 50)
        else:
            import_week.place(x = 1170, y = 100, width = 120, height = 50)
        export_schedule = ttk.Button(root, text = "Export", command = lambda: ScheduleHandler.export(Week().weekList))
        if root.winfo_width() > 1900:
            export_schedule.place(x = root.winfo_width() - 300, y = 170, width = 120, height = 50)
        else:
            export_schedule.place(x = 1170, y = 170, width = 120, height = 50)

        clear = ttk.Button(root, text = "Wyczyść", command = lambda: ScheduleHandler.clear())
        if root.winfo_width() > 1900:
            clear.place(x = root.winfo_width() - 300, y = 470, width = 120, height = 50)
        else:
            clear.place(x = 1170, y = 470, width = 120, height = 50)

        y=0
        for x in range(0,16):
            nazwy = View.ward.print_initials(x)
            nazwa = tk.Label(root,text=nazwy, bd=1, relief=SOLID, font=("Consolas"))
            if root.winfo_width() >1900:
                nazwa.place(x= root.winfo_width()/2 -700/2+ y+38,y=50,width=30,height=20)

            else:
                nazwa.place(x = root.winfo_width()/2-700/2 + 38 + y, y = 50, width = 30, height = 20)

            y=y+33

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
            dni = ttk.Label(frame, text=_dni[x%7])
            dni.grid(row=x,column=0, ipadx=40, sticky='e')


        generate = ttk.Button(root, text = "Generate", command = lambda: Fill_Window(View.ward,root,frame))
        if root.winfo_width()>1900:
            generate.place(x = root.winfo_width() - 300, y = 400, width = 120, height = 50)
        else:
            generate.place(x = 1170, y = 400, width = 120, height = 50)

        root.mainloop()