from src.Exporter import Exporter
import unittest

class testExport(unittest.TestCase):
    def testExportJoin(self):
        days = []
        days.append("Test")
        self.assertEqual("Test", ''.join(days[0]))


if __name__ == "__main__":
    unittest.main()