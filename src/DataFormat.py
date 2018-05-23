class DataFormat:
    def code(self,days):
        for i,line in enumerate(days):
            for j,x in enumerate(line):
                if x == "E":
                    days[i][j] = "1"
                elif x == "D":
                    days[i][j] = "2"
                elif x == "L":
                    days[i][j] = "3"
                elif x == "N":
                    days[i][j] = "4"
                else:
                    days[i][j] = "5"
        return days
    def decode(self,days):
        for i,line in enumerate(days):
            for j,x in enumerate(line):
                if x == "1":
                    days[i][j] = "E"
                elif x == "2":
                    days[i][j] = "D"
                elif x == "3":
                    days[i][j] = "L"
                elif x == "4":
                    days[i][j] = "N"
                else:
                    days[i][j] = "-"
        return days
    def transpose(self,days):
        return [[row[i] for row in days] for i in range(len(days[0]))]
