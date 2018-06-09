from tkinter import filedialog

class Importer:
    def doimport(self):
        filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        f = open(filename, 'r')
        days = []
        for line in f:

            if len(line) in [17, 8, 36]:

                nurse = []
                for i in range(0, len(line)-1):
                    nurse.append(line[i])
                days.append(nurse)
            else:
                print("Nieprawidlowy format danych")

        f.close()

        dataform = DataFormat()
        days = dataform.decode(days)
        if len(days) == 16:
            daysTranspose = dataform.transpose()
            return daysTranspose
        else:
            return days