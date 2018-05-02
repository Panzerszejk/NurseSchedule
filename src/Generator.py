from .Schedule import Schedule
from .Week import Week


class Generator:
    def generate(self, schedule=None):
        if schedule is None:
            pass
            #code for no parameter call
        elif isinstance(schedule, Week):
            week=schedule  #namechange for consistency, not necessary
            #code for week parameter call
        elif isinstance(schedule, Schedule):
            pass
            #code for schedule parameter call

