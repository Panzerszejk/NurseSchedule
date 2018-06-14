from tkinter import filedialog
from src.DataFormat import DataFormat

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
            daysTranspose = dataform.transpose(days)
        else:
            daysTranspose = days

        k = 0
        for j in range(len(daysTranspose[0])):
            for i in range(len(daysTranspose)):
                if daysTranspose[i][j] == "N":
                    k = k + 1
                    if k > 1:
                        if (i + 1) <= (len(daysTranspose) - 1):
                            if daysTranspose[i + 1][j] == "-":
                                daysTranspose[i + 1][j] = "x"
                                if daysTranspose[i + 2][j] == "-" and ((i + 2) <= (len(daysTranspose) - 1)):
                                    daysTranspose[i + 2][j] = "x"
                            else:
                                continue
                        else:
                            k = 0
                else:
                    k = 0

        k = 0
        for j in range(len(daysTranspose[0])):
            for i in range(len(daysTranspose)):
                if (daysTranspose[i][j] != "-") and (daysTranspose[i][j] != "x") :
                    k = k + 1
                    if k > 4:
                        if (i + 1) <= (len(daysTranspose) - 1):
                            if daysTranspose[i + 1][j] == "-":
                                daysTranspose[i + 1][j] = 'x'
                                k = 0
                            else:
                                continue
                        else:
                            k = 0
                else:
                    k = 0

        return daysTranspose
