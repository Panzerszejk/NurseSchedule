import unittest
from src.Schedule import Schedule
from src.Week import Week
from src.ConstraintChecker import ConstraintChecker
from src.Ward import Ward
from src.Nurse import Nurse
from src.Constraint import Constraint


class FirstSoftConstraint(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule()
        self.schedule.scheduleList = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['E','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','D','-'],#friday 5
                                      ['-','-','-','-','-','E','N','D','N','E','L','D','E','-','-','-'],
                                      ['-','-','-','-','-','N','E','N','D','L','E','E','D','-','-','-'],#sunday 7
                                      ['-','-','-','-','E','-','-','-','-','-','-','N','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','D','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','N','-','-','-','-','-','-','-'],
                                      ['L','N','L','N','L','N','L','N','-','-','-','-','-','-','-','-'],#friday
                                      ['E','E','D','D','L','L','N','N','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#14
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','D','-','-','E','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','N','-','-','-','-','-','-','-','-','-'],
                                      ['-','L','L','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['E','E','E','E','D','D','D','D','E','E','E','E','D','D','D','D'],#friday
                                      ['E','D','L','N','E','D','L','N','E','D','L','N','E','D','L','N'],
                                      ['-','-','-','-','-','-','-','-','E','D','L','N','E','D','L','N'],#21
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday
                                      ['-','-','-','-','-','-','-','-','E','D','L','N','E','D','L','N'],
                                      ['E','D','L','N','E','D','L','N','E','D','L','N','E','D','L','N'],#28
                                      ['E','D','L','N','E','D','L','N','-','-','-','-','L','E','N','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','N','-','-','-','-','-','L','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','L','D','L','N','E','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#35
                                      ]
        self.imported = Week()
        self.imported.importedWeek = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday 5
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#sunday 7
                                      ]
        self.ward = Ward()
        self.ward.add_nurse(Nurse(0,"Janina", "Bąk",23,22,True))
        self.ward.add_nurse(Nurse(1,"Joanna", "Rabarbar",23,22,True))
        self.ward.add_nurse(Nurse(2,"Agnieszka","Hohenstein",23,22,True))
        self.ward.add_nurse(Nurse(3,"Ilona","Wojarska",23,22,True))
        self.ward.add_nurse(Nurse(4,"Adrianna","Markowska",23,22,True))
        self.ward.add_nurse(Nurse(5,"Marianna","terkalska",23,22,True))
        self.ward.add_nurse(Nurse(6,"Anna","Gronkiewicz",23,22,True))
        self.ward.add_nurse(Nurse(7,"Zofia","Górska",23,22,True))
        self.ward.add_nurse(Nurse(8,"Anastazja","Kuśmider",23,22,True))
        self.ward.add_nurse(Nurse(9,"Karolina","Igrekowska",23,22,True))
        self.ward.add_nurse(Nurse(10,"Martyna","Oleń",23,22,True))
        self.ward.add_nurse(Nurse(11,"Alicja","Gruszkiewicz",23,22,False))
        self.ward.add_nurse(Nurse(12,"Zyta","Bożek",20,20,True))
        self.ward.add_nurse(Nurse(13,"Brunhilda","Palas",13,12,True))
        self.ward.add_nurse(Nurse(14,"Kinga","Zegrzyńska",13,12,True))
        self.ward.add_nurse(Nurse(15,"Jagoda","Malinowska",13,12,True))
        #setting only constraint 1 with value, rest will be omitted in summary constraint weight
        self.ward.add_constraint(Constraint(1,1000))
        self.ward.add_constraint(Constraint(3,0))
        self.ward.add_constraint(Constraint(5,0))
        self.ward.add_constraint(Constraint(7,0))
        self.ward.add_constraint(Constraint(9,0))
        self.ward.add_constraint(Constraint(13,0))

    def test_constraint_value(self):
        self.constchecker = ConstraintChecker(self.ward,self.schedule,self.imported)
        self.constchecker.check()
        self.assertEqual(self.constchecker.totalWeight, 16000)#16 non-full weekends coded in scheule table

    def tearDown(self):
        del self.ward
        del self.constchecker
        del self.schedule
        del self.imported


class ThirdSoftConstraint(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule()
        self.schedule.scheduleList = [['N','N','N','N','N','N','-','N','N','N','N','N','N','N','N','N'],#monday 1
                                      ['-','N','N','-','N','N','-','-','N','N','-','N','N','-','N','N'],
                                      ['-','-','N','-','-','N','-','-','-','N','-','-','N','-','-','N'],
                                      ['-','E','E','D','L','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','N','N','N','N','N','N','-','-','-','-','-','-','-','-','-'],#friday 5
                                      ['-','-','N','-','-','-','N','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','N','N','-','-','-','-','-','-','-','-'],#sunday 7
                                      ['-','-','-','-','-','-','N','N','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','N','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','N','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','N','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#14
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#21
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#28
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#35
                                      ]
        self.imported = Week()
        self.imported.importedWeek = [['-','-','-','-','-','N','-','-','-','-','-','-','-','-','-','N'],#monday 1
                                      ['-','-','-','-','E','N','-','-','-','-','-','-','-','-','E','N'],
                                      ['-','-','-','-','-','N','-','-','-','-','-','-','-','-','-','N'],
                                      ['-','-','-','N','N','D','-','-','-','-','-','-','-','N','N','D'],
                                      ['-','-','N','-','N','E','N','-','-','-','-','-','N','-','N','E'],#friday 5
                                      ['-','E','N','N','N','N','N','-','-','-','-','E','N','N','N','N'],
                                      ['N','N','N','N','E','N','N','-','-','-','N','N','N','N','E','N'],#sunday 7
                                      ]
        self.ward = Ward()
        self.ward.add_nurse(Nurse(0,"Janina", "Bąk",23,22,True))
        self.ward.add_nurse(Nurse(1,"Joanna", "Rabarbar",23,22,True))
        self.ward.add_nurse(Nurse(2,"Agnieszka","Hohenstein",23,22,True))
        self.ward.add_nurse(Nurse(3,"Ilona","Wojarska",23,22,True))
        self.ward.add_nurse(Nurse(4,"Adrianna","Markowska",23,22,True))
        self.ward.add_nurse(Nurse(5,"Marianna","terkalska",23,22,True))
        self.ward.add_nurse(Nurse(6,"Anna","Gronkiewicz",23,22,True))
        self.ward.add_nurse(Nurse(7,"Zofia","Górska",23,22,True))
        self.ward.add_nurse(Nurse(8,"Anastazja","Kuśmider",23,22,True))
        self.ward.add_nurse(Nurse(9,"Karolina","Igrekowska",23,22,True))
        self.ward.add_nurse(Nurse(10,"Martyna","Oleń",23,22,True))
        self.ward.add_nurse(Nurse(11,"Alicja","Gruszkiewicz",23,22,False))
        self.ward.add_nurse(Nurse(12,"Zyta","Bożek",20,20,True))
        self.ward.add_nurse(Nurse(13,"Brunhilda","Palas",13,12,True))
        self.ward.add_nurse(Nurse(14,"Kinga","Zegrzyńska",13,12,True))
        self.ward.add_nurse(Nurse(15,"Jagoda","Malinowska",13,12,True))
        #setting only constraint 1 with value, rest will be omitted in summary constraint weight
        self.ward.add_constraint(Constraint(1,0))
        self.ward.add_constraint(Constraint(3,1000))
        self.ward.add_constraint(Constraint(5,0))
        self.ward.add_constraint(Constraint(7,0))
        self.ward.add_constraint(Constraint(9,0))
        self.ward.add_constraint(Constraint(13,0))

    def test_constraint_value(self):
        self.constchecker = ConstraintChecker(self.ward,self.schedule,self.imported)
        self.constchecker.check()
        self.assertEqual(self.constchecker.totalWeight, 16000)#16 separate or more than 3 nightshifts, including imported week
        #should only be counted for nurses index 0-12 as is

    def tearDown(self):
        del self.ward
        del self.constchecker
        del self.schedule
        del self.imported


class FifthSoftConstraint(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule()
        self.schedule.scheduleList = [['-','-','E','-','E','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['E','-','-','E','E','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','D','-','E','E','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','E','-','E','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','E','-','E','-','-','-','-','-','-','-','-','-'],#friday 5
                                      ['-','D','-','-','-','-','D','-','-','-','-','-','-','-','-','-'],
                                      ['-','E','-','-','D','-','N','-','-','-','-','-','-','-','-','-'],#sunday 7
                                      ['-','L','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','L','-','E','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','E','D','-','-','-','-','-','-','-','-','-'],
                                      ['-','D','-','-','N','E','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday
                                      ['-','-','-','-','E','E','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','D','D','-','-','-','-','-','-','-','-','-','-'],#14
                                      ['-','-','-','-','E','E','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','E','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','N','E','-','-','E','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','N','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','N','-','-','-','-','-','-','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#21
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#28
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#35
                                      ]
        self.imported = Week()
        self.imported.importedWeek = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday 5
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#sunday 7
                                      ]
        self.ward = Ward()
        self.ward.add_nurse(Nurse(0,"Janina", "Bąk",23,22,True))
        self.ward.add_nurse(Nurse(1,"Joanna", "Rabarbar",23,22,True))
        self.ward.add_nurse(Nurse(2,"Agnieszka","Hohenstein",23,22,True))
        self.ward.add_nurse(Nurse(3,"Ilona","Wojarska",23,22,True))
        self.ward.add_nurse(Nurse(4,"Adrianna","Markowska",23,22,True))
        self.ward.add_nurse(Nurse(5,"Marianna","terkalska",23,22,True))
        self.ward.add_nurse(Nurse(6,"Anna","Gronkiewicz",23,22,True))
        self.ward.add_nurse(Nurse(7,"Zofia","Górska",23,22,True))
        self.ward.add_nurse(Nurse(8,"Anastazja","Kuśmider",23,22,True))
        self.ward.add_nurse(Nurse(9,"Karolina","Igrekowska",23,22,True))
        self.ward.add_nurse(Nurse(10,"Martyna","Oleń",23,22,True))
        self.ward.add_nurse(Nurse(11,"Alicja","Gruszkiewicz",23,22,False))
        self.ward.add_nurse(Nurse(12,"Zyta","Bożek",20,20,True))
        self.ward.add_nurse(Nurse(13,"Brunhilda","Palas",13,12,True))
        self.ward.add_nurse(Nurse(14,"Kinga","Zegrzyńska",13,12,True))
        self.ward.add_nurse(Nurse(15,"Jagoda","Malinowska",13,12,True))
        #setting only constraint 1 with value, rest will be omitted in summary constraint weight
        self.ward.add_constraint(Constraint(1,0))
        self.ward.add_constraint(Constraint(3,0))
        self.ward.add_constraint(Constraint(5,100))
        self.ward.add_constraint(Constraint(7,0))
        self.ward.add_constraint(Constraint(9,0))
        self.ward.add_constraint(Constraint(13,0))

    def test_constraint_value(self):
        self.constchecker = ConstraintChecker(self.ward,self.schedule,self.imported)
        self.constchecker.check()
        self.assertEqual(self.constchecker.totalWeight, 500)#5 times constraint broken

    def tearDown(self):
        del self.ward
        del self.constchecker
        del self.schedule
        del self.imported


class SeventhSoftConstraint(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule()
        self.schedule.scheduleList = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','E','E'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','D','E'],#friday 5
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#sunday 7
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','E','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','E','-','-','D','-','-','-'],
                                      ['-','-','-','-','N','-','-','-','-','D','-','-','L','-','E','N'],
                                      ['-','-','-','-','N','-','-','-','-','E','-','-','E','E','D','N'],
                                      ['-','-','-','-','N','-','E','-','-','D','-','-','D','D','-','-'],#friday
                                      ['-','-','-','-','N','-','D','-','-','E','-','-','-','D','-','-'],
                                      ['-','-','-','-','-','-','E','-','-','D','-','-','-','-','E','-'],#14
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','N','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','-','E'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','-','E'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','-'],#21
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','N','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','N','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','N','N'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','N','N'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','-','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#28
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','-','E'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','-','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','E','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','D','N'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','L','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','E'],#35
                                      ]
        self.imported = Week()
        self.imported.importedWeek = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday 5
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#sunday 7
                                      ]
        self.ward = Ward()
        self.ward.add_nurse(Nurse(0,"Janina", "Bąk",23,22,True))
        self.ward.add_nurse(Nurse(1,"Joanna", "Rabarbar",23,22,True))
        self.ward.add_nurse(Nurse(2,"Agnieszka","Hohenstein",23,22,True))
        self.ward.add_nurse(Nurse(3,"Ilona","Wojarska",23,22,True))
        self.ward.add_nurse(Nurse(4,"Adrianna","Markowska",23,22,True))
        self.ward.add_nurse(Nurse(5,"Marianna","terkalska",23,22,True))
        self.ward.add_nurse(Nurse(6,"Anna","Gronkiewicz",23,22,True))
        self.ward.add_nurse(Nurse(7,"Zofia","Górska",23,22,True))
        self.ward.add_nurse(Nurse(8,"Anastazja","Kuśmider",23,22,True))
        self.ward.add_nurse(Nurse(9,"Karolina","Igrekowska",23,22,True))
        self.ward.add_nurse(Nurse(10,"Martyna","Oleń",23,22,True))
        self.ward.add_nurse(Nurse(11,"Alicja","Gruszkiewicz",23,22,False))
        self.ward.add_nurse(Nurse(12,"Zyta","Bożek",20,20,True))
        self.ward.add_nurse(Nurse(13,"Brunhilda","Palas",13,12,True))
        self.ward.add_nurse(Nurse(14,"Kinga","Zegrzyńska",13,12,True))
        self.ward.add_nurse(Nurse(15,"Jagoda","Malinowska",13,12,True))
        #setting only constraint 1 with value, rest will be omitted in summary constraint weight
        self.ward.add_constraint(Constraint(1,0))
        self.ward.add_constraint(Constraint(3,0))
        self.ward.add_constraint(Constraint(5,0))
        self.ward.add_constraint(Constraint(7,10))
        self.ward.add_constraint(Constraint(9,0))
        self.ward.add_constraint(Constraint(13,0))

    def test_constraint_value(self):
        self.constchecker = ConstraintChecker(self.ward,self.schedule,self.imported)
        self.constchecker.check()
        self.assertEqual(self.constchecker.totalWeight, 40)#16 non-full weekends coded in scheule table

    def tearDown(self):
        del self.ward
        del self.constchecker
        del self.schedule
        del self.imported


class NinthSoftConstraint(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule()
        self.schedule.scheduleList = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','-','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','E','D'],#friday 5
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','-','-'],#sunday 7
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','-','N'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','N'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','-'],#14
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','-','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','D','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','D','N'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','D','N'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','D','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#21
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','-','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','E','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#28
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','D','E','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','E','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','D'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#35
                                      ]
        self.imported = Week()
        self.imported.importedWeek = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday 5
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#sunday 7
                                      ]
        self.ward = Ward()
        self.ward.add_nurse(Nurse(0,"Janina", "Bąk",23,22,True))
        self.ward.add_nurse(Nurse(1,"Joanna", "Rabarbar",23,22,True))
        self.ward.add_nurse(Nurse(2,"Agnieszka","Hohenstein",23,22,True))
        self.ward.add_nurse(Nurse(3,"Ilona","Wojarska",23,22,True))
        self.ward.add_nurse(Nurse(4,"Adrianna","Markowska",23,22,True))
        self.ward.add_nurse(Nurse(5,"Marianna","terkalska",23,22,True))
        self.ward.add_nurse(Nurse(6,"Anna","Gronkiewicz",23,22,True))
        self.ward.add_nurse(Nurse(7,"Zofia","Górska",23,22,True))
        self.ward.add_nurse(Nurse(8,"Anastazja","Kuśmider",23,22,True))
        self.ward.add_nurse(Nurse(9,"Karolina","Igrekowska",23,22,True))
        self.ward.add_nurse(Nurse(10,"Martyna","Oleń",23,22,True))
        self.ward.add_nurse(Nurse(11,"Alicja","Gruszkiewicz",23,22,False))
        self.ward.add_nurse(Nurse(12,"Zyta","Bożek",20,20,True))
        self.ward.add_nurse(Nurse(13,"Brunhilda","Palas",13,12,True))
        self.ward.add_nurse(Nurse(14,"Kinga","Zegrzyńska",13,12,True))
        self.ward.add_nurse(Nurse(15,"Jagoda","Malinowska",13,12,True))
        #setting only constraint 1 with value, rest will be omitted in summary constraint weight
        self.ward.add_constraint(Constraint(1,0))
        self.ward.add_constraint(Constraint(3,0))
        self.ward.add_constraint(Constraint(5,0))
        self.ward.add_constraint(Constraint(7,0))
        self.ward.add_constraint(Constraint(9,10))
        self.ward.add_constraint(Constraint(13,0))

    def test_constraint_value(self):
        self.constchecker = ConstraintChecker(self.ward,self.schedule,self.imported)
        self.constchecker.check()
        self.assertEqual(self.constchecker.totalWeight, 70)#16 non-full weekends coded in scheule table

    def tearDown(self):
        del self.ward
        del self.constchecker
        del self.schedule
        del self.imported


class ThirteenthSoftConstraint(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule()
        self.schedule.scheduleList = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday 5
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','E','D','L','N','-','-','-','-','-','-','-','-','-','-'],#sunday 7
                                      ['-','-','N','N','N','N','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','E','D','L','N','-','-','-','-','-','E','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','N','-','E','-','-'],
                                      ['-','-','N','N','N','N','-','-','-','-','-','-','-','N','-','-'],#friday
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','E','-','-','-','-','-','-','-'],#14
                                      ['-','-','-','-','-','-','-','-','N','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','E','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','N','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday
                                      ['-','-','-','D','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','D','-','-','-','-','-','-','-','-','-','-','-','-'],#21
                                      ['-','-','-','D','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','D','-','N','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','D','-','-','-','-','E','-','-','-','-','-','-','D','-','-'],
                                      ['-','N','-','-','-','-','E','-','-','-','-','-','-','D','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','E','-','-'],#friday
                                      ['-','-','-','-','-','-','N','-','-','-','-','-','-','N','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#28
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#35
                                      ]
        self.imported = Week()
        self.imported.importedWeek = [['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#monday 1
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#friday 5
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
                                      ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],#sunday 7
                                      ]
        self.ward = Ward()
        self.ward.add_nurse(Nurse(0,"Janina", "Bąk",23,22,True))
        self.ward.add_nurse(Nurse(1,"Joanna", "Rabarbar",23,22,True))
        self.ward.add_nurse(Nurse(2,"Agnieszka","Hohenstein",23,22,True))
        self.ward.add_nurse(Nurse(3,"Ilona","Wojarska",23,22,True))
        self.ward.add_nurse(Nurse(4,"Adrianna","Markowska",23,22,True))
        self.ward.add_nurse(Nurse(5,"Marianna","terkalska",23,22,True))
        self.ward.add_nurse(Nurse(6,"Anna","Gronkiewicz",23,22,True))
        self.ward.add_nurse(Nurse(7,"Zofia","Górska",23,22,True))
        self.ward.add_nurse(Nurse(8,"Anastazja","Kuśmider",23,22,True))
        self.ward.add_nurse(Nurse(9,"Karolina","Igrekowska",23,22,True))
        self.ward.add_nurse(Nurse(10,"Martyna","Oleń",23,22,True))
        self.ward.add_nurse(Nurse(11,"Alicja","Gruszkiewicz",23,22,False))
        self.ward.add_nurse(Nurse(12,"Zyta","Bożek",20,20,True))
        self.ward.add_nurse(Nurse(13,"Brunhilda","Palas",13,12,True))
        self.ward.add_nurse(Nurse(14,"Kinga","Zegrzyńska",13,12,True))
        self.ward.add_nurse(Nurse(15,"Jagoda","Malinowska",13,12,True))
        #setting only constraint 1 with value, rest will be omitted in summary constraint weight
        self.ward.add_constraint(Constraint(1,0))
        self.ward.add_constraint(Constraint(3,0))
        self.ward.add_constraint(Constraint(5,0))
        self.ward.add_constraint(Constraint(7,0))
        self.ward.add_constraint(Constraint(9,0))
        self.ward.add_constraint(Constraint(13,1))

    def test_constraint_value(self):
        self.constchecker = ConstraintChecker(self.ward,self.schedule,self.imported)
        self.constchecker.check()
        self.assertEqual(self.constchecker.totalWeight, 5)#16 non-full weekends coded in scheule table

    def tearDown(self):
        del self.ward
        del self.constchecker
        del self.schedule
        del self.imported


if __name__ == '__main__':
    unittest.main()
