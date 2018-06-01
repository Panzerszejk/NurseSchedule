"""
import unittest
from src.Schedule import Schedule
from src.Checker import Checker

class TestChecker(unittest.TestCase):
    def test_checkEBlank(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['-']
        self.assertTrue(ch.checkE(sch, 0, 0))
    def test_checkEE(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['E']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkED(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['D']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkEL(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['L']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkEN(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['N']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkEnE(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nE']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkEnD(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nD']
        self.assertTrue(ch.checkE(sch, 0, 0))
    def test_checkEnL(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nL']
        self.assertTrue(ch.checkE(sch, 0, 0))
    def test_checkEnN(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nN']
        self.assertTrue(ch.checkE(sch, 0, 0))
    def test_checkEnED(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nED']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkEnEL(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nEL']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkEnEN(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nEN']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkEnDL(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nDL']
        self.assertTrue(ch.checkE(sch, 0, 0))
    def test_checkEnDN(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nDN']
        self.assertTrue(ch.checkE(sch, 0, 0))
    def test_checkEnLN(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nLN']
        self.assertTrue(ch.checkE(sch, 0, 0))
    def test_checkEnDLN(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nDLN']
        self.assertTrue(ch.checkE(sch, 0, 0))
    def test_checkEnELN(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nELN']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkEnEDN(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nEDN']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkEnEDL(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['nEDL']
        self.assertFalse(ch.checkE(sch, 0, 0))
    def test_checkx(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = ['x']
        self.assertFalse(ch.checkE(sch, 0, 0))
"""
    def test_oldCheckE(self):
        ch = Checker()
        sch = Schedule()
        sch.scheduleList = [['E', 'D', 'L', 'N'],
                            ['nDL', 'nL', 'nDLN', '-'],
                            ['x', 'nE', 'nD', 'nN']]
        controlList = [[False, False, False, False],
                        [True, True, True, True],
                        [False, False, True, True]]
        for i in range(3):
            for j in range(4):
                condNew = ch.checkE(sch, i , j)
                self.assertEqual(condNew, controlList[i][j])"""

if __name__ == '__main__':
    unittest.main()"""