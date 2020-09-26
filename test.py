import unittest

from letra_dni import LetraDni

class TestLetraDNI(unittest.TestCase):
    def test_12345678(self):
        myDni = LetraDni("12345678")
        self.assertEqual(myDni.calculate(), "Z")
    def test_87654321(self):
        myDni = LetraDni("87654321")
        self.assertEqual(myDni.calculate(), "X")

if __name__ == '__main__':
    unittest.main()