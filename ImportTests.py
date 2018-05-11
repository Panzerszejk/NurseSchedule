from src.Importer import Importer
import unittest

class testImport(unittest.TestCase):
    def testImportNone(self):
        imp = Importer()
        cos = imp.doimport()
        self.assertIsNotNone(cos)

    def testImport(self):
        imp = Importer()
        cos = len(imp.doimport())
        self.assertEqual(cos, 35)

    def testImportS(self):
        imp = Importer()
        for i in range(17):
            cos = len(imp.doimport()[i])
            self.assertEqual(cos, 17)

if __name__ == "__main__":
    unittest.main()