import numpy

class ScheduleDisplayer:
    def __init__(self,schedule=None):
        self.schedule=schedule
    def display(self):
        print(numpy.matrix(self.schedule))
