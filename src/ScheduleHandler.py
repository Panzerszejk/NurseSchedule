from .Importer import Importer
from .Week import Week
from .Schedule import Schedule
from .Generator import Generator
from .Exporter import Exporter


class ScheduleHandler:

    imported = None

    @staticmethod
    def importer(var):
        imp = Importer()
        if var == "week":
            sched = Week()
            sched.importedWeek = imp.doimport()
            ScheduleHandler.imported = sched
        elif var == "schedule":
            sched = Schedule()
            sched.importedSchedule = imp.doimport()
            ScheduleHandler.imported = sched
        else:
            sched = None
            print("No argument given")

    @staticmethod
    def export(sched):  #sched is a class Schedule object
        exp = Exporter()
        exp.export(sched)

    @staticmethod
    def generate(ward):  #imported is a class Schedule or Week object, can be Null
        gen = Generator()
        if ScheduleHandler.imported is None:
            return gen.generate(ward)
        elif isinstance(ScheduleHandler.imported, Week) or isinstance(ScheduleHandler.imported,Schedule):
            return gen.generate(ward,ScheduleHandler.imported)

    @staticmethod
    def accept():
        pass

    @staticmethod
    def clear():
        pass

