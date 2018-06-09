from src.DataFormat import DataFormat
import unittest


class DataFormatCodeTest(unittest.TestCase):
    
    def setUp(self):
        self.df = DataFormat()
        self.codedTable = [["1","2","3"],["4","5","1"],["2","3","4"]]
        self.decodedTable = [["E","D","L"],["N","-","E"],["D","L","N"]]
        
    def testDataFormatCode(self):
        self.assertEqual(self.codedTable, self.df.code(self.decodedTable))
        
    def tearDown(self):
        del self.codedTable
        del self.decodedTable


if __name__ == '__main__':
    unittest.main()
