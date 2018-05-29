import numpy
import random as ran
from .ScheduleDisplayer import ScheduleDisplayer

class ReferenceTable:
    def __init__(self):
        self.ref = [[3 for x in range(3)] for y in range(35)]
        weekends = [5,6,12,13,19,20,26,27,33,34]
        for i in range(len(weekends)):
            temp = weekends.pop(ran.randint(0, len(weekends)-1))
            for j in range(3):
                self.ref[temp][j] = 2
        self.display = ScheduleDisplayer(self)

