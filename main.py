from .src.ScheduleHandler import ScheduleHandler
from .src.ScheduleDisplayer import ScheduleDisplayer
from .src.Nurse import Nurse
from .src.Ward import Ward
from .src.Constraint import Constraint
from .src.ConstraintChecker import ConstraintChecker


def main():
    ward = Ward()
    ward.add_nurse(Nurse(0,"Full Time",23,22,True))
    ward.add_nurse(Nurse(1,"Full Time",23,22,True))
    ward.add_nurse(Nurse(2,"Full Time",23,22,True))
    ward.add_nurse(Nurse(3,"Full Time",23,22,True))
    ward.add_nurse(Nurse(4,"Full Time",23,22,True))
    ward.add_nurse(Nurse(5,"Full Time",23,22,True))
    ward.add_nurse(Nurse(6,"Full Time",23,22,True))
    ward.add_nurse(Nurse(7,"Full Time",23,22,True))
    ward.add_nurse(Nurse(8,"Full Time",23,22,True))
    ward.add_nurse(Nurse(9,"Full Time",23,22,True))
    ward.add_nurse(Nurse(10,"Full Time",23,22,True))
    ward.add_nurse(Nurse(11,"Niepracujaca Late",23,22,False))
    ward.add_nurse(Nurse(12,"32 godzinowa",20,20,True))
    ward.add_nurse(Nurse(13,"Part Time",13,12,True))
    ward.add_nurse(Nurse(14,"Part Time",13,12,True))
    ward.add_nurse(Nurse(15,"Part Time",13,12,True))

    ward.add_constraint(Constraint(1,1000))
    ward.add_constraint(Constraint(1,1000))
    ward.add_constraint(Constraint(1,100))
    ward.add_constraint(Constraint(1,10))
    ward.add_constraint(Constraint(1,10))
    ward.add_constraint(Constraint(1,1))

    handler = ScheduleHandler()
    schedImported = handler.importer("schedule") #returns schedule object with imported data
    weekImported = handler.importer("week")      #returns week object with imported data
    MainSchedule1 = handler.generate(ward, schedImported) #returns schedule object with data generated using imported schedule
    MainSchedule2 = handler.generate(ward, weekImported)  #returns schedule object with data generated using imported week

    softchecker = ConstraintChecker(ward,MainSchedule1,weekImported) #checking soft constraints for MainSchedule1
    softchecker.check()
    weight = softchecker.get_totalWeight()      #total weight of unfulfilled soft constraints, less is better


    displayer = ScheduleDisplayer(MainSchedule1)
    displayer.display()
    #displaying schedule MainSchedule1

if __name__ == "__main__":
    main()
