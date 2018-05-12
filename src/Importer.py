from tkinter import filedialog

class Importer:
    def doimport(self):
        filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        f = open(filename, 'r')
        days = []
        for line in f:
            if len(line) != 17:
                print("Blad nie ma danych dla 16 pielegniarek")
            else:
                nurse = []
                for i in range(0, len(line)-1):
                    nurse.append(line[i])
                days.append(nurse)
        f.close()
        return days
