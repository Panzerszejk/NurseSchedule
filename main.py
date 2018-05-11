from src.ScheduleHandler import ScheduleHandler
from src.ScheduleDisplayer import ScheduleDisplayer
from src.Nurse import Nurse
from src.Ward import Ward
from src.Week import Week
from src.Constraint import Constraint
from src.ConstraintChecker import ConstraintChecker
from src.View import View
import tkinter as tk


if __name__ == "__main__":

    ward = Ward()
    ward.add_nurse(Nurse(0,"Janina", "Bąk",23,22,True))
    ward.add_nurse(Nurse(1,"Joanna", "Rabarbar",23,22,True))
    ward.add_nurse(Nurse(2,"Agnieszka","Hohenstein",23,22,True))
    ward.add_nurse(Nurse(3,"Ilona","Wojarska",23,22,True))
    ward.add_nurse(Nurse(4,"Adrianna","Markowska",23,22,True))
    ward.add_nurse(Nurse(5,"Marianna","terkalska",23,22,True))
    ward.add_nurse(Nurse(6,"Anna","Gronkiewicz",23,22,True))
    ward.add_nurse(Nurse(7,"Zofia","Górska",23,22,True))
    ward.add_nurse(Nurse(8,"Anastazja","Kuśmider",23,22,True))
    ward.add_nurse(Nurse(9,"Karolina","Igrekowska",23,22,True))
    ward.add_nurse(Nurse(10,"Martyna","Oleń",23,22,True))
    ward.add_nurse(Nurse(11,"Alicja","Gruszkiewicz",23,22,False))
    ward.add_nurse(Nurse(12,"Zyta","Bożek",20,20,True))
    ward.add_nurse(Nurse(13,"Brunhilda","Palas",13,12,True))
    ward.add_nurse(Nurse(14,"Kinga","Zegrzyńska",13,12,True))
    ward.add_nurse(Nurse(15,"Jagoda","Malinowska",13,12,True))

    ward.add_constraint(Constraint(1,1000))
    ward.add_constraint(Constraint(3,1000))
    ward.add_constraint(Constraint(5,100))
    ward.add_constraint(Constraint(7,10))
    ward.add_constraint(Constraint(9,10))
    ward.add_constraint(Constraint(13,1))

    ScheduleHandler.importer("schedule") #returns schedule object with imported data
    MainSchedule1 = ScheduleHandler.generate(ward) #returns schedule object with data generated using imported schedule

    softchecker = ConstraintChecker(ward,MainSchedule1,ScheduleHandler.imported) #checking soft constraints for MainSchedule1
    softchecker.check()
    weight = softchecker.get_totalWeight()      #total weight of unfulfilled soft constraints, less is better


    displayer = ScheduleDisplayer(MainSchedule1)
    displayer.display()
    #displaying schedule MainSchedule1


    View.import_ward(ward)
    View = View()




