from tkinter import *
import tkinter as tk
from .Array import Array


class View(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        _dni = ["Poniedzialek", "Wtorek", "Sroda", "Czwartek", "Piatek", "Sobota", "Niedziela"]
        y=0
        for x in range(0,16):
            nazwa = tk.Label(master,text=Array.tablica[x][0], bd=1, relief=SOLID)
            nazwa.place(x=260+y,y=50,width=40,height=20)
            y=y+49

        def fun(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=970,height=self.master.winfo_height()-200)


        na_dni = tk.Frame(master)
        na_dni.place(x=100,y=100)
        canvas = Canvas(na_dni)
        frame = Frame(canvas)
        scrollbar = Scrollbar(na_dni, orient=VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",fun)

        for x in range(0,35):
            dni = tk.Label(frame, text=_dni[x%7])
            dni.grid(row=x,column=0, ipadx=40, sticky=E)
            for i in range(0,16):
                lbl = tk.Label(frame,relief=SOLID, bd=1)
                lbl.grid(row=x,column=i+1,ipadx=18)

                if str(Array.tablica[i][2]) == "D" and str(Array.tablica[i][0].split('P')[1]) == str(i+1) and str(Array.tablica[i][1])==str(_dni[x%7]):
                    lbl.configure(text="D")
                elif str(Array.tablica[i][2]) == "E" and str(Array.tablica[i][0].split('P')[1]) == str(i+1) and str(Array.tablica[i][1])==str(_dni[x%7]):
                    lbl.configure(text="E")
                elif str(Array.tablica[i][2]) == "N" and str(Array.tablica[i][0].split('P')[1]) == str(i+1) and str(Array.tablica[i][1])==str(_dni[x%7]):
                    lbl.configure(text="N")
                else:
                    lbl.configure(text=3*" ")













