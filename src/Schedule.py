from .ScheduleDisplayer import ScheduleDisplayer
from .ScheduleHandler import ScheduleHandler


class Schedule:
    def __init__(self):
        self.ScheduleList = [[0 for x in range(16)] for y in range(35)]
        self.ScheduleDisplay = ScheduleDisplayer()
        self.ScheduleHandle = ScheduleHandler()
