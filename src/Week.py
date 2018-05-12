class Week:
    def __init__(self):
        self.weekList = [[0 for i in range(16)] for j in range(7)]      #possibly unnecessary
        self.displayer = ScheduleDisplayer(self)
        #self.importedWeek = []      #week imported from txt file