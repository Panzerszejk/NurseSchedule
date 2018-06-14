import unittest
from src.Schedule import Schedule
from src.Week import Week
from src.ConstraintChecker import ConstraintChecker
from src.Ward import Ward
from src.Nurse import Nurse
from src.Constraint import Constraint


class HardConstTesting(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule()
        self.schedule.scheduleList = [['E','L','E','-','D','D','L','L','-','-','E','D','-','N','-','-'],#monday 1
                                      ['D','L','-','-','D','-','L','L','E','E','-','D','E','N','-','-'],
                                      ['-','-','-','L','E','E','L','L','D','D','N','-','D','-','E','-'],
                                      ['-','-','L','L','-','E','-','L','-','E','N','D','E','-','D','D'],
                                      ['E','N','L','L','D','D','-','L','-','E','-','D','-','-','-','E'],#friday 5
                                      ['E','N','L','L','-','D','E','-','D','-','-','-','-','-','-','-'],
                                      ['E','N','L','L','-','-','E','-','D','-','D','-','-','-','-','-'],#sunday 7
                                      ['E','-','-','-','L','E','-','D','D','N','-','D','-','E','L','L'],
                                      ['D','-','E','D','L','-','E','D','-','N','E','L','-','L','-','-'],
                                      ['-','-','E','L','L','D','D','D','E','-','E','-','-','L','N','-'],#9
                                      ['D','D','E','L','-','E','L','E','-','-','D','L','-','-','N','-'],
                                      ['E','D','D','L','-','-','L','E','N','E','D','L','-','-','-','-'],#friday
                                      ['-','L','-','-','E','D','-','-','N','E','-','-','L','-','-','D'],
                                      ['-','L','-','-','E','D','-','-','N','E','-','-','L','-','-','D'],#14
                                      ['D','L','-','D','L','E','-','E','-','D','-','-','-','E','L','N'],
                                      ['E','L','-','E','-','D','E','L','-','D','D','-','L','-','-','N'],
                                      ['N','-','D','L','D','E','-','L','-','D','E','-','L','E','-','-'],
                                      ['N','E','L','L','D','-','D','-','D','-','E','E','L','-','-','-'],
                                      ['-','L','L','L','D','E','N','-','D','E','-','D','-','-','-','E'],#friday
                                      ['-','-','L','-','-','-','N','D','D','-','E','E','-','-','L','-'],
                                      ['-','-','L','-','-','-','N','D','D','-','E','E','-','-','L','-'],#21
                                      ['E','L','-','N','D','-','-','-','-','D','E','L','L','E','-','D'],
                                      ['-','L','E','N','D','L','-','E','D','D','E','-','-','-','L','-'],
                                      ['E','-','D','-','N','L','E','-','D','L','D','E','-','-','L','-'],
                                      ['D','E','L','-','N','L','D','-','E','-','E','D','-','-','L','-'],
                                      ['D','D','L','L','-','L','E','N','E','-','-','E','D','-','-','-'],#friday
                                      ['D','D','-','-','-','-','E','N','-','E','-','-','-','L','-','L'],
                                      ['-','-','-','D','-','-','E','N','-','E','-','-','D','L','-','L'],#28
                                      ['-','L','-','-','E','D','D','-','D','E','E','L','N','L','-','-'],
                                      ['D','-','E','E','L','D','-','-','-','E','-','L','N','L','-','D'],
                                      ['-','D','L','-','L','E','E','-','D','E','-','N','-','L','-','D'],
                                      ['D','L','-','L','L','D','E','E','D','-','E','N','-','-','-','-'],
                                      ['D','L','N','L','L','D','E','E','E','-','D','-','-','-','-','-'],
                                      ['E','-','N','L','-','-','-','D','-','L','E','-','-','-','D','-'],
                                      ['E','-','N','L','-','-','-','D','-','L','E','-','-','-','D','-'],#35
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
        self.ward.add_constraint(Constraint(3,1000))
        self.ward.add_constraint(Constraint(5,100))
        self.ward.add_constraint(Constraint(7,10))
        self.ward.add_constraint(Constraint(9,10))
        self.ward.add_constraint(Constraint(13,1))

    def test_constraint_value(self):
        self.constchecker = ConstraintChecker(self.ward,self.schedule,self.imported)
        self.constchecker.check()
        self.constchecker.checkHarder()
        print(self.constchecker.infoTable)
        print("-------------------------------")
        print(self.constchecker.HardInfoTable)
        self.assertEqual(self.constchecker.totalWeight, 16000)#16 non-full weekends coded in scheule table

    def tearDown(self):
        del self.ward
        del self.constchecker
        del self.schedule
        del self.imported


if __name__ == '__main__':
    unittest.main()
