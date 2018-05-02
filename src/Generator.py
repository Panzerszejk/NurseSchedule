from .Schedule import Schedule
from .Week import Week


class Generator:
    @staticmethod
    def generate(self, ward, sched=None):
        output = Schedule() #write data to output object
        if sched is None:
            pass
            #code for no parameter call (no data from previous weeks)
        elif isinstance(sched, Week):
            week=sched  #namechange for consistency, not necessary
            #code for imported week parameter call (data from previous week)
        elif isinstance(sched, Schedule):
            pass
            #code for imported schedule parameter call (data from whole previous schedule)
        return output

#sched is an object of class Week or Schedule depending on what is imported!