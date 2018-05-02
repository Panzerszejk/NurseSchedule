from .Importer import Importer
from .Week import Week
from .Schedule import Schedule
from .Generator import Generator
from .Exporter import Exporter


class ScheduleHandler:
    def importer(self, var):
        if var == "week":
            sched = Week()
            sched.importedWeek = Importer.doimport()
        elif var == "schedule":
            sched = Schedule()
            sched.importedSchedule = Importer.doimport()
        else:
            sched = None
            print("No argument given")
        return sched

    def export(self, sched):  #sched is a class Schedule object
        Exporter.export(sched)

    def generate(self, ward, imported = None):  #imported is a class Schedule or Week object, can be Null
        if imported is None:
            return Generator.generate(ward)
        else:
            return Generator.generate(ward,imported)

    def accept(self):
        pass

    def clear(self):
        pass

