from .Importer import Importer


class ConstraintChecker:
    def __init__(self,ward=None,schedule=None):
        self.totalWeight=0
        self.schedule=schedule
        self.ward=ward
        self.imported=Importer.doimport()

    def check(self, constraint):
        if constraint.number == 1:  #pierwszy constraint
            for nurse in range(16):
                for day in range(35):
                    if day % 7 == 4:  #jest piątek
                        shiftcount = 0
                        friday = self.schedule[day][nurse]
                        saturday = self.schedule[day+1][nurse]
                        sunday = self.schedule[day+2][nurse]
                        if friday == 'L':
                            shiftcount += 1
                        if friday == 'N':
                            shiftcount += 1
                        if saturday != '-':
                            shiftcount += 1
                        if sunday == 'N':
                            shiftcount += 1
                        if 3 > shiftcount > 0:
                            self.totalWeight += constraint.weight
        elif constraint.number == 3:  #trzeci constraint
            for nurse in range(16):
                if self.ward.nurses[nurse].minShifts > 15:  #więcej od 15 bo pielęgniary pół-zmianowe mają max 13, dlaczego więc 15? bo tak
                    nightseries=0
                    for daysImport in range(3):  #checking last 3 days of previous schedule for night shift series
                        previousschedday = self.imported[34-daysImport][nurse]
                        if previousschedday == 'N':
                            nightseries+=1
                        else:
                            break
                    for day in range(35):
                        currentday = self.schedule[day][nurse]
                        if currentday == 'N':
                            nightseries+=1
                        else:
                            if nightseries == 1 or nightseries == 4:
                                self.totalWeight += constraint.weight
                            elif nightseries == 5:
                                self.totalWeight += constraint.weight*2
                            elif nightseries == 6:
                                self.totalWeight += constraint.weight*3
                            nightseries=0
        elif constraint.number == 5:
            pass
            self.totalWeight+=constraint.weight
        elif constraint.number == 7:
            pass
            self.totalWeight+=constraint.weight
        elif constraint.number == 9:
            pass
            self.totalWeight+=constraint.weight
        elif constraint.number == 13:
            pass
            self.totalWeight+=constraint.weight

    def get_totalWeight(self):
        return self.totalWeight

    def set_totalWeight(self,weight):
        self.totalWeight=weight

    def import_schedule(self,schedule):
        self.schedule=schedule

    def import_ward(self, ward):
        self.ward=ward