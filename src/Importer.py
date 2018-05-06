class Importer:
    @staticmethod
    def doimport(self,filename):
        f = open(filename, 'r')
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
        return days


imp = Importer()
imp.doimport()
