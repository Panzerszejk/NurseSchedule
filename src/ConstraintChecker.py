from .Schedule import Schedule
from .Week import Week


class ConstraintChecker:
    def __init__(self, ward = None, schedule = None, imported = None):
        self.totalWeight = 0
        """
        dla infotable pierwsza kolumna to numer constraina, 
        druga kolumna to ilosc naruszen danego constraina, 
        a trzecia kolumna to waga wszystkich tych naruszen dla poszczegolnego constraina
        """
        self.infoTable = [[1,0,0],
                          [3,0,0],
                          [5,0,0],
                          [7,0,0],
                          [9,0,0],
                          [13,0,0]]
        self.HardInfoTable = [[1,0],
                              [2,0],
                              [3,0],
                              [4,0],
                              [5,0],
                              [6,0],
                              [7,0],
                              [8,0],
                              [9,0]]
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
                        self.infoTable[0][2] += self.ward.constraints[0].weight
                        self.infoTable[0][1] += 1
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
                            self.infoTable[1][2] += self.ward.constraints[1].weight
                            self.infoTable[1][1] += 1
                        elif nightseries == 5:
                            self.totalWeight += self.ward.constraints[1].weight*2
                            self.infoTable[1][2] += self.ward.constraints[1].weight*2
                            self.infoTable[1][1] += 1
                        elif nightseries == 6:
                            self.totalWeight += self.ward.constraints[1].weight*3
                            self.infoTable[1][2] += self.ward.constraints[1].weight*3
                            self.infoTable[1][1] += 1
                        nightseries=0
        #fifth constraint
        for nurse in range(16):
            workseries = 0
            for day in range(34):
                currentday = self.schedule.scheduleList[day][nurse]
                nextday = self.schedule.scheduleList[day+1][nurse]
                if currentday != '-':
                    workseries += 1
                    if currentday == 'N':
                        workseries = 0
                else:
                    if nextday != '-' and workseries > 1:
                        self.totalWeight += self.ward.constraints[2].weight
                        self.infoTable[2][2] += self.ward.constraints[2].weight
                        self.infoTable[2][1] += 1
                    workseries = 0
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
                            self.infoTable[3][2] += self.ward.constraints[3].weight*(shiftonweekcount-3)
                            self.infoTable[3][1] += 1
                        elif shiftonweekcount < 2:  #acceptable number is 2-3
                            self.totalWeight += self.ward.constraints[3].weight*(2-shiftonweekcount)
                            self.infoTable[3][2] += self.ward.constraints[3].weight*(2-shiftonweekcount)
                            self.infoTable[3][1] += 1
                        #print("week has: "+str(shiftonweekcount))
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
                                self.infoTable[4][2] += self.ward.constraints[4].weight*(shiftcount-3)
                                self.infoTable[4][1] += 1
                            elif shiftcount < 2:  #acceptable number is 2-3
                                self.totalWeight += self.ward.constraints[4].weight*(2-shiftcount)
                                self.infoTable[4][2] += self.ward.constraints[4].weight*(2-shiftcount)
                                self.infoTable[4][1] += 1
                        shiftcount = 0
        #thirteenth constraint
        for nurse in range(16):
            if isinstance(self.imported, Week):
                previousday = self.imported.importedWeek[6][nurse]
            elif isinstance(self.imported, Schedule):
                previousday = self.imported.importedSchedule[34][nurse]
            else:
                previousday = None
                #print("Error, need data from previous schedule") #even false data will do
            for day in range(34): #1 day less
                currentday = self.schedule.scheduleList[day][nurse]
                if previousday == 'E' and currentday == 'N':
                    self.totalWeight += self.ward.constraints[5].weight
                    self.infoTable[5][2] += self.ward.constraints[5].weight
                    self.infoTable[5][1] += 1
                previousday = currentday

    def get_totalWeight(self):
        return self.totalWeight

    """
    error codes:
    -1      shifts not covered properly on sunday and saturday   checkHard('all') <- must have 'all' parameter!
    -2      shifts not covered properly on monday to friday      checkHard('all') <- must have 'all' parameter!
    -3      too many shifts (all shifts apply)
    -4      too many night shifts
    -5      too few weekends off duty
    -6      standard resting period after Late shift broken
    -7      standard resting period after Night shift broken
    -8      resting period after night series broken
    -9      work series too long

    checkHard() returns a tuple: [error code, value at which error occured (day or nurse)]
    """
    def checkHard(self,var=None):
        if var == 'all':
            #all shifts covered
            for day in range(35):
                early = 0
                day = 0
                late = 0
                night = 0
                for nurse in range(16):
                    currentday = self.schedule.scheduleList[day][nurse]
                    if currentday == 'E':
                        early += 1
                    if currentday == 'D':
                        day += 1
                    if currentday == 'L':
                        late += 1
                    if currentday == 'N':
                        night += 1
                if day%7 == 5 or day%7 == 6: #sun and sat
                    if early != 2 or day != 2 or late != 2 or night != 1:
                        print("shifts not covered properly at day:"+str(day))
                        return -1,day
                else:                       #mon - fri
                    if early != 3 or day != 3 or late != 3 or night != 1:
                        print("shifts not covered properly at day:"+str(day))
                        return -2,day
        #number of shifts within limit and nightshifts
        for nurse in range(16):
            shifts = 0
            nightshifts = 0
            for day in range(35):
                currentday = self.schedule.scheduleList[day][nurse]
                if currentday != '-':
                    shifts += 1
                if currentday == 'N':
                    nightshifts += 1
            if shifts > self.ward.nurses[nurse].maxShifts:
                print("too many shifts for nurse:"+str(nurse))
                return -3,nurse
            if nightshifts > 3:
                print("too many night shifts for nurse:"+str(nurse))
                return -4,nurse
        #weekends off duty
        for nurse in range(16):
            weekendoffduty = 0
            for day in range(35):
                if day%7 == 4: #jest piatek
                    friday = self.schedule.scheduleList[day][nurse]
                    saturday = self.schedule.scheduleList[day+1][nurse]
                    sunday = self.schedule.scheduleList[day+2][nurse]
                    if friday != 'N' and saturday == '-' and sunday == '-':
                        weekendoffduty += 1
            if weekendoffduty < 2:
                print("too few weekends off duty for nurse:"+str(nurse))
                return -5,nurse
        #resting periods
        for nurse in range(16):
            for day in range(34):
                currentday = self.schedule.scheduleList[day][nurse]
                nextday = self.schedule.scheduleList[day+1][nurse]
                if currentday == 'L':
                    if nextday == 'E' or nextday == 'D':
                        print("resting period broken for nurse:"+str(nurse)+" on day:"+str(day))
                        return -6,nurse
                elif currentday == 'N':
                    if nextday == 'E' or nextday == 'D' or nextday == 'L':
                        print("resting period broken for nurse:"+str(nurse)+" on day:"+str(day))
                        return -7,nurse
        #series of nightshifts rest and consecutive shifts limit
        for nurse in range(16):
            restRequired = False
            restDays = 0
            nightSeries = 0
            workSeries = 0
            for daysImport in range(7):  #checking last 7 days of previous schedule for night shift and work shift series
                if isinstance(self.imported, Week):
                    previousschedday = self.imported.importedWeek[6-daysImport][nurse]
                elif isinstance(self.imported, Schedule):
                    previousschedday = self.imported.importedSchedule[34-daysImport][nurse]
                else:
                    previousschedday = None
                if previousschedday == 'N':
                    nightSeries += 1
                if previousschedday != '-':
                    workSeries += 1
                else:
                    break
            for day in range(35):
                currentday = self.schedule.scheduleList[day][nurse]
                if currentday == 'N':
                    nightSeries += 1
                else:                           #series broken
                    if nightSeries > 1:
                        restRequired = True
                    nightSeries = 0
                    if restRequired and currentday != '-':
                        print("resting period after night series broken for nurse:"+str(nurse)+" on day:"+str(day))
                        return -8,nurse
                    elif restRequired:
                        restDays += 1
                        if restDays > 1:
                            restRequired = False
                            restDays = 0
                if currentday != '-':
                    workSeries += 1
                    if workSeries > 6:
                        print("work series too long for nurse:"+str(nurse)+" on day:"+str(day))
                        return -9,nurse
                else:
                    workSeries = 0
        return 0

    def checkHarder(self):

            #all shifts covered
        for day in range(35):
            early_shift = 0
            day_shift = 0
            late_shift = 0
            night_shift = 0
            for nurse in range(16):
                currentday = self.schedule.scheduleList[day][nurse]
                if currentday == 'E':
                    early_shift += 1
                if currentday == 'D':
                    day_shift += 1
                if currentday == 'L':
                    late_shift += 1
                if currentday == 'N':
                    night_shift += 1
            if day%7 == 5 or day%7 == 6: #sun and sat
                if early_shift != 2 or day_shift != 2 or late_shift != 2 or night_shift != 1:
                    self.HardInfoTable[0][1] += 1
                    print(day,early_shift,day_shift,late_shift,night_shift)
            else:                       #mon - fri
                if early_shift != 3 or day_shift != 3 or late_shift != 3 or night_shift != 1:
                    self.HardInfoTable[1][1] += 1
                    print(day,early_shift,day_shift,late_shift,night_shift)

        #number of shifts within limit and nightshifts
        for nurse in range(16):
            shifts = 0
            nightshifts = 0
            for day in range(35):
                currentday = self.schedule.scheduleList[day][nurse]
                if currentday != '-':
                    shifts += 1
                if currentday == 'N':
                    nightshifts += 1
            if shifts > self.ward.nurses[nurse].maxShifts:
                self.HardInfoTable[2][1] += 1
            if nightshifts > 3:
                self.HardInfoTable[3][1] += 1
        #weekends off duty
        for nurse in range(16):
            weekendoffduty = 0
            for day in range(35):
                if day%7 == 4: #jest piatek
                    friday = self.schedule.scheduleList[day][nurse]
                    saturday = self.schedule.scheduleList[day+1][nurse]
                    sunday = self.schedule.scheduleList[day+2][nurse]
                    if friday != 'N' and saturday == '-' and sunday == '-':
                        weekendoffduty += 1
            if weekendoffduty < 2:
                self.HardInfoTable[4][1] += 1
        #resting periods
        for nurse in range(16):
            for day in range(34):
                currentday = self.schedule.scheduleList[day][nurse]
                nextday = self.schedule.scheduleList[day+1][nurse]
                if currentday == 'L':
                    if nextday == 'E' or nextday == 'D':
                        self.HardInfoTable[5][1] += 1
                        print("day "+str(day)+"   nurse "+str(nurse))
                elif currentday == 'N':
                    if nextday == 'E' or nextday == 'D' or nextday == 'L':
                        self.HardInfoTable[6][1] += 1
        #series of nightshifts rest and consecutive shifts limit
        for nurse in range(16):
            restRequired = False
            restDays = 0
            nightSeries = 0
            workSeries = 0
            for daysImport in range(7):  #checking last 7 days of previous schedule for night shift and work shift series
                if isinstance(self.imported, Week):
                    previousschedday = self.imported.importedWeek[6-daysImport][nurse]
                elif isinstance(self.imported, Schedule):
                    previousschedday = self.imported.importedSchedule[34-daysImport][nurse]
                else:
                    previousschedday = None
                if previousschedday == 'N':
                    nightSeries += 1
                if previousschedday != '-':
                    workSeries += 1
                else:
                    break
            for day in range(35):
                currentday = self.schedule.scheduleList[day][nurse]
                if currentday == 'N':
                    nightSeries += 1
                else:                           #series broken
                    if nightSeries > 1:
                        restRequired = True
                    nightSeries = 0
                    if restRequired and currentday != '-':
                        self.HardInfoTable[7][1] += 1
                    elif restRequired:
                        restDays += 1
                        if restDays > 1:
                            restRequired = False
                            restDays = 0
                if currentday != '-':
                    workSeries += 1
                    if workSeries > 6:
                        self.HardInfoTable[8][1] += 1
                else:
                    workSeries = 0
        return 0

    def set_totalWeight(self,weight):
        self.totalWeight=weight

    def import_schedule(self,schedule):
        self.schedule=schedule

    def import_ward(self, ward):
        self.ward=ward