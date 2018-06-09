from tkinter import messagebox
import tkinter as tk

class LogsWindow:
    def __init__(self,infotable,hardbreach):
        errorcode,value = hardbreach
        text = ""
        sum = 0
        for line in infotable:
            text += "Constraint " + str(line[0]) + " - " + str(line[1]) + " breaches. Cost: " + str(line[2]) + ".\n"
            sum += line[2]
        text += "Total cost: " + str(sum) + "\n\n"
        if errorcode < 0:
            if errorcode == -1:
                text += "Hard constraint breach!\nShifts not covered properly on weekend.\nPosition: " +str(value)+ ".\n"
            elif errorcode == -2:
                text += "Hard constraint breach!\nShifts not covered properly on workdays.\nPosition: " +str(value)+ ".\n"
            elif errorcode == -3:
                text += "Hard constraint breach!\nToo many shifts.\nPosition: " +str(value)+ ".\n"
            elif errorcode == -4:
                text += "Hard constraint breach!\nToo many night shifts.\nPosition: " +str(value)+ ".\n"
            elif errorcode == -5:
                text += "Hard constraint breach!\nToo few weekends off duty.\nPosition: " +str(value)+ ".\n"
            elif errorcode == -6:
                text += "Hard constraint breach!\nStandard resting period after Late shift broken.\nPosition: " +str(value)+ ".\n"
            elif errorcode == -7:
                text += "Hard constraint breach!\nStandard resting period after Night shift broken.\nPosition: " +str(value)+ ".\n"
            elif errorcode == -8:
                text += "Hard constraint breach!\nResting period after night series broken.\nPosition: " +str(value)+ ".\n"
            elif errorcode == -9:
                text += "Hard constraint breach!\nWork series too long.\nPosition: " +str(value)+ ".\n"
        else:
            text += "No hard constraint breaches."
        tk.messagebox.showwarning("Constraints", text)