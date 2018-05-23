import unittest
from src.Nurse import Nurse


class MyTestCase(unittest.TestCase):
    def test_number(self):
        self.nurse_test = Nurse(self, 1, 'Janina', 'Bak', 5, 2, True)
        self.assertEqual(self.nurse_test.number, 1)

    def test_name(self):
     self.nurse_test = Nurse(self, 1, 'Janina', 'Bak', 5, 2, True)
     self.assertEqual(self.nurse_test.name, 'Janina')

    def test_surname(self):
        self.nurse_test = Nurse(self, 1, 'Janina', 'Bak', 5, 2, True)
        self.assertEqual(self.nurse_test.surname, 'Bak')


    def test_maxshifts(self):
        self.nurse_test = Nurse(self, 1, 'Janina', 'Bak', 5, 2, True)
        self.assertEqual(self.nurse_test.maxShifts, 5)


    def test_minshifts(self):
        self.nurse_test = Nurse(self, 1, 'Janina', 'Bak', 5, 2, True)
        self.assertEqual(self.nurse_test.minShifts, 2)

    def test_nightshifts(self):
        self.nurse_test = Nurse(self, 1, 'Janina', 'Bak', 5, 2, True)
        self.assertEqual(self.nurse_test.workingNights, True)

if __name__ == '__main__':
    unittest.main()