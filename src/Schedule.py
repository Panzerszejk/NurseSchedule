from .ScheduleDisplayer import ScheduleDisplayer

class Schedule:
    def __init__(self):
        self.scheduleList = [['-' for x in range(16)] for y in range(35)]   #schedule where we generate data into
        self.displayer = ScheduleDisplayer(self)
        self.importedSchedule = []      #whole schedule imported from txt file
        for i in range(35):
            self.scheduleList[i][11] = 'nL'