from .View import View
from tkinter import Menu,filedialog
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()

    root.attributes("-fullscreen",True)
    root.update()

    wyjdz = tk.Button(root, text="Wyjscie", command=root.destroy)
    wyjdz.place(x=root.winfo_width() - 200, y=root.winfo_height() - 100, width=170, height=50)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Import", command=lambda: )
    menubar.add_cascade(label="File", menu=filemenu)
    master.config(menu=menubar)

    View.View(root)


    root.mainloop()


    def ImportMenu(self):
        filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        doimport(filename)