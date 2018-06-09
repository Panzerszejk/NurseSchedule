import unittest
from src.SymbolTable import SymbolTable


class TestSymbolTable(unittest.TestCase):
    def test_length(self):      #checks whether or not I forgot some symbol during copying/adding/etc
        self.assertEqual(20, len(SymbolTable.eSymbolsBlocked))
        self.assertEqual(20, len(SymbolTable.dSymbolsBlocked))
        self.assertEqual(20, len(SymbolTable.lSymbolsBlocked))
        self.assertEqual(20, len(SymbolTable.nSymbolsBlocked))

if __name__ == '__main__':
    unittest.main()
