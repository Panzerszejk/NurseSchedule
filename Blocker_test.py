import unittest
from src.SymbolTable import SymbolTable
from src.Blocker import Blocker
from src.Schedule import Schedule

class TestBlocker(unittest.TestCase):
    def test_blockE(self):
        sch = Schedule()
        sch.scheduleList = [['E', 'D', 'L', 'N'],
                            ['nDL', 'nL', 'nDLN', '-'],
                            ['x', 'nE', 'nD', 'nN']]

        output = Schedule()
        output.scheduleList = [['E', 'D', 'L', 'N'],
                            ['nEDL', 'nEL', 'x', 'nE'],
                            ['x', 'nE', 'nED', 'nEN']]
        bl = Blocker()
        for i in range(3):
            for j in range(4):
                bl.blockE(sch, i , j)
                self.assertEqual(sch.scheduleList[i][j], output.scheduleList[i][j])

    def test_blockD(self):
        sch = Schedule()
        sch.scheduleList = [['E', 'D', 'L', 'N'],
                            ['nEL', 'nL', 'nELN', '-'],
                            ['x', 'nE', 'nD', 'nN']]

        output = Schedule()
        output.scheduleList = [['E', 'D', 'L', 'N'],
                            ['nEDL', 'nDL', 'x', 'nD'],
                            ['x', 'nED', 'nD', 'nDN']]
        bl = Blocker()
        for i in range(3):
            for j in range(4):
                bl.blockD(sch, i , j)
                self.assertEqual(sch.scheduleList[i][j], output.scheduleList[i][j])

    def test_blockL(self):
        sch = Schedule()
        sch.scheduleList = [['E', 'D', 'L', 'N'],
                            ['nDN', 'nL', 'nEDN', '-'],
                            ['x', 'nE', 'nD', 'nN']]

        output = Schedule()
        output.scheduleList = [['E', 'D', 'L', 'N'],
                            ['nDLN', 'nL', 'x', 'nL'],
                            ['x', 'nEL', 'nDL', 'nLN']]
        bl = Blocker()
        for i in range(3):
            for j in range(4):
                bl.blockL(sch, i , j)
                self.assertEqual(sch.scheduleList[i][j], output.scheduleList[i][j])

    def test_blockN(self):
        sch = Schedule()
        sch.scheduleList = [['E', 'D', 'L', 'N'],
                            ['nDL', 'nL', 'nEDL', '-'],
                            ['x', 'nE', 'nD', 'nN']]

        output = Schedule()
        output.scheduleList = [['E', 'D', 'L', 'N'],
                            ['nDLN', 'nLN', 'x', 'nN'],
                            ['x', 'nEN', 'nDN', 'nN']]
        bl = Blocker()
        for i in range(3):
            for j in range(4):
                bl.blockN(sch, i , j)
                self.assertEqual(sch.scheduleList[i][j], output.scheduleList[i][j])

if __name__ == '__main__':
    unittest.main()
