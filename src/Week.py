from ScheduleDisplayer import ScheduleDisplayer

class Week:
    def __init__(self):
        self.week = [[x for i in range(16)] for j in range(7)]
        self.displayer = ScheduleDisplayer()
"""
    def display:
        for i in range(16):
            for j in range(7):
                print(self.week[i][j])
"""
