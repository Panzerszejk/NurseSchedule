from tkinter import messagebox
import tkinter as tk

class LogsWindow:
    def __init__(self,infotable):
        text = ""
        sum = 0
        for line in infotable:
            text += "Constraint " + str(line[0]) + " - " + str(line[1]) + " breaches. Cost: " + str(line[2]) + ".\n"
            sum += line[2]
        text += "Total cost: " + str(sum)
        tk.messagebox.showwarning("Constraints", text)
