class Importer:
    def doimport(self):
        # with open('test.txt','r') as f:
        #     days = f.read()

        f = open('test.txt', 'r')
        days = []
        for line in f:
            #print(line,len(line))
            if len(line) != 17:
                print("Blad nie ma danych dla 16 pielegniarek")
            else:
                nurse = []
                for i in range(0, len(line)):
                    nurse.append(line[i])
                days.append(nurse)
                #print(days)
        print(days)
        return days


if __name__=='__main__':
    Importer().doimport()