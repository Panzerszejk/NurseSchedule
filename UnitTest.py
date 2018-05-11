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


if __name__ == '__main__':
    unittest.main()
