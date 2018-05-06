from .Importer import Importer
from .Week import Week
from .Schedule import Schedule
from .Generator import Generator
from .Exporter import Exporter


class ScheduleHandler:
    def importer(self, var):
        imp = Importer()
        if var == "week":
            sched = Week()
            sched.importedWeek = imp.doimport()
        elif var == "schedule":
            sched = Schedule()
            sched.importedSchedule = imp.doimport()
        else:
            sched = None
            print("No argument given")
        return sched

    def export(self, sched):  #sched is a class Schedule object
        exp = Exporter()
        exp.export(sched)

    def generate(self, ward, imported = None):  #imported is a class Schedule or Week object, can be Null
        gen = Generator()
        if imported is None:
            return gen.generate(ward)
        else:
            return gen.generate(ward,imported)

    def accept(self):
        pass

    def clear(self):
        pass

