class Schedule:
    def __init__(self):
        self.scheduleList = [[0 for x in range(16)] for y in range(35)]   #schedule where we generate data into
        self.importedSchedule = []      #whole schedule imported from txt file
