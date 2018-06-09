from .Schedule import Schedule
from .Week import Week
from .ReferenceTable import ReferenceTable
from .Assigner import Assigner
import sys

"""
    Now this code as coarse as  possible, and will be "objectified" next week
"""

def cleanup(sched):         #DZIALA GIT
    for i in range(35):
        for j in range(16):
            if (sched.scheduleList[i][j] == 'E' or  sched.scheduleList[i][j] == 'D' or sched.scheduleList[i][j] == 'L' or sched.scheduleList[i][j] == 'N'):
                pass
            else:
                sched.scheduleList[i][j] = '-'
    return sched

class Generator:
    def generate(self, ward, sched=None):
        sys.setrecursionlimit(10000)
        output = Schedule() #write data to output object
        ass = Assigner()
        if sched is None:
            output = Schedule()
            ref = ReferenceTable()
            output = ass.assignWeekends(output)
            output = ass.assignNightShifts(output)
            for i in range(5):
                output, ref = ass.assignShifts(output, ref, i)
            output = cleanup(output)
            #display(ref)
            output.displayer.display()
        elif isinstance(sched, Week):
            week=sched  #namechange for consistency, not necessary
            #code for imported week parameter call (data from previous week)
        elif isinstance(sched, Schedule):
            pass
            #code for imported schedule parameter call (data from whole previous schedule)
        return output

#sched is an object of class Week or Schedule depending on what is imported!
