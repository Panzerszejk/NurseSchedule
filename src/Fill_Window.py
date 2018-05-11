import tkinter as tk


class Fill_Window:
    def __init__(self,View,frame):
        _dni = ["Poniedzialek", "Wtorek", "Sroda", "Czwartek", "Piatek", "Sobota", "Niedziela"]
        for x in range(0,35):
            dni = tk.Label(frame, text=_dni[x%7])
            dni.grid(row=x,column=0, ipadx=40, sticky='e')
            for i in range(0,16):
                lbl = tk.Label(frame,relief='solid', bd=1)
                lbl.grid(row=x,column=i+1,ipadx=18)

                if str(View.sched[x][i]) == "D":
                    lbl.configure(text="D")
                elif str(View.sched[x][i]) == "E":
                    lbl.configure(text="E")
                elif str(View.sched[x][i]) == "N":
                    lbl.configure(text="N")
                elif str(View.sched[x][i]) == "L":
                    lbl.configure(text="L")
                else:
                    lbl.configure(text=3*" ")
