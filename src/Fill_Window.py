import tkinter as tk


class Fill_Window:
    def __init__(self,View,frame):
        for x in range(0,35):
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
