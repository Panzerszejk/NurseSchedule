from tkinter import filedialog

class Importer:
    def doimport(self):
        filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        f = open(filename, 'r')
        #f = open("test.txt", 'r')
        days = []
        for line in f:
            print(line,len(line))
            if len(line) != 17:
                print("Blad nie ma danych dla 16 pielegniarek")
            else:
                nurse = []
                for i in range(0, len(line)):
                    nurse.append(line[i])
                days.append(nurse)
                print(days)
        f.close()
        return days
