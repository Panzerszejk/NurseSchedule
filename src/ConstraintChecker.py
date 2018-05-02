from .Schedule import Schedule
from .Week import Week


class ConstraintChecker:
    def __init__(self, ward = None, schedule = None, imported = None):
        self.totalWeight = 0
        self.schedule = schedule
        self.ward = ward
        self.imported = imported

    def check(self):
        #first constraint
        for nurse in range(16):
            for day in range(35):
                if day % 7 == 4:  #jest piątek
                    shiftcount = 0
                    friday = self.schedule.scheduleList[day][nurse]
                    saturday = self.schedule.scheduleList[day+1][nurse]
                    sunday = self.schedule.scheduleList[day+2][nurse]
                    if friday == 'L':
                        shiftcount += 1
                    if friday == 'N':
                        shiftcount += 1
                    if saturday != '-':
                        shiftcount += 1
                    if sunday == 'N':
                        shiftcount += 1
                    if 3 > shiftcount > 0:
                        self.totalWeight += self.ward.constraints[0].weight
        #third constraint
        for nurse in range(16):
            if self.ward.nurses[nurse].minShifts > 15:  #więcej od 15 bo pielęgniary pół-zmianowe mają max 13, dlaczego więc 15? bo tak
                nightseries=0
                for daysImport in range(3):  #checking last 3 days of previous schedule for night shift series
                    if isinstance(self.imported, Week):
                        previousschedday = self.schedule.importedSchedule[6-daysImport][nurse]
                    elif isinstance(self.imported, Schedule):
                        previousschedday = self.schedule.importedSchedule[34-daysImport][nurse]
                    else:
                        previousschedday = None
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
                            self.totalWeight += self.ward.constraints[1].weight
                        elif nightseries == 5:
                            self.totalWeight += self.ward.constraints[1].weight*2
                        elif nightseries == 6:
                            self.totalWeight += self.ward.constraints[1].weight*3
                        nightseries=0


    def get_totalWeight(self):
        return self.totalWeight

    def set_totalWeight(self,weight):
        self.totalWeight=weight

    def import_schedule(self,schedule):
        self.schedule=schedule

    def import_ward(self, ward):
        self.ward=ward