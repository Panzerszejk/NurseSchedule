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
                    if sunday != '-':
                        shiftcount += 1
                    if 2 > shiftcount > 0:
                        self.totalWeight += self.ward.constraints[0].weight
        #third constraint
        for nurse in range(16):
            if self.ward.nurses[nurse].minShifts > 15:  #więcej od 15 bo pielęgniary pół-zmianowe mają max 13, dlaczego więc 15? bo tak
                nightseries=0
                for daysImport in range(3):  #checking last 3 days of previous schedule for night shift series
                    if isinstance(self.imported, Week):
                        previousschedday = self.imported.importedWeek[6-daysImport][nurse]
                    elif isinstance(self.imported, Schedule):
                        previousschedday = self.imported.importedSchedule[34-daysImport][nurse]
                    else:
                        previousschedday = None
                    if previousschedday == 'N':                                                                                      
                        nightseries+=1
                    else:
                        break
                for day in range(35):
                    currentday = self.schedule.scheduleList[day][nurse]
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
        #fifth constraint
        for nurse in range(16):
            restcount = 0
            eligableflag = False
            for day in range(35):
                currentday = self.schedule.scheduleList[day][nurse]
                if currentday != '-':
                    if restcount == 1:
                        self.totalWeight += self.ward.constraints[2].weight
                    restcount=0
                    if currentday != 'N':
                        eligableflag = True
                    else:
                        eligableflag = False
                elif eligableflag:
                    restcount+=1
        #seventh constraint
        for nurse in range(16):
            if self.ward.nurses[nurse].minShifts < 15:  #part-time nurses only
                shiftonweekcount = 0
                for day in range(35):
                    currentday = self.schedule.scheduleList[day][nurse]
                    if currentday != '-':
                        shiftonweekcount += 1
                    if day % 7 == 6:  #niedziela
                        if shiftonweekcount > 3:
                            self.totalWeight += self.ward.constraints[3].weight*(shiftonweekcount-3)
                        elif shiftonweekcount < 2:  #acceptable number is 2-3
                            self.totalWeight += self.ward.constraints[3].weight*(2-shiftonweekcount)
                        shiftonweekcount = 0
        #ninth constraint
        for nurse in range(16):
            if self.ward.nurses[nurse].minShifts < 15:  #part-time nurses only
                shiftcount = 0
                for daysImport in range(3):  #checking last 3 days of previous schedule for night shift series
                    if isinstance(self.imported, Week):
                        previousschedday = self.imported.importedWeek[6-daysImport][nurse]
                    elif isinstance(self.imported, Schedule):
                        previousschedday = self.imported.importedSchedule[34-daysImport][nurse]
                    else:
                        previousschedday = None
                    if previousschedday != '-':
                        shiftcount += 1
                    else:
                        break
                for day in range(35):
                    currentday = self.schedule.scheduleList[day][nurse]
                    if currentday != '-':
                        shiftcount += 1
                    else:
                        if shiftcount > 0 and day != 0:  #avoiding situation when after imported shift series is rest day
                            if shiftcount > 3:
                                self.totalWeight += self.ward.constraints[4].weight*(shiftcount-3)
                            elif shiftcount < 2:  #acceptable number is 2-3
                                self.totalWeight += self.ward.constraints[4].weight*(2-shiftcount)
                        shiftcount = 0
        #thirteenth constraint
        for nurse in range(16):
            if isinstance(self.imported, Week):
                previousday = self.imported.importedWeek[6][nurse]
            elif isinstance(self.imported, Schedule):
                previousday = self.imported.importedSchedule[34][nurse]
            else:
                previousday = None
                print("Error, need data from previous schedule") #even false data will do
            for day in range(34): #1 day less
                currentday = self.schedule.scheduleList[day][nurse]
                if previousday == 'E' and currentday == 'N':
                    self.totalWeight += self.ward.constraints[5].weight
                previousday = currentday

    def get_totalWeight(self):
        return self.totalWeight

    def set_totalWeight(self,weight):
        self.totalWeight=weight

    def import_schedule(self,schedule):
        self.schedule=schedule

    def import_ward(self, ward):
        self.ward=ward