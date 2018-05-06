from .View import View
import tkinter as tk


root = tk.Tk()
root.attributes("-fullscreen",True)
root.update()
wyjdz = tk.Button(root, text="Wyjscie", command=root.destroy)
wyjdz.place(x=root.winfo_width() - 200, y=root.winfo_height() - 100, width=170, height=50)
View = View(root)
root.mainloop()

#this file is executed before main and should consist of imports etc. , the above instructions should probably go into main?