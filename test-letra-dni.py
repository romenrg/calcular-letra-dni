import unittest

from letra_dni import letra_dni

class TestLetraDNI(unittest.TestCase):
    def test_12345678(self):
        self.assertEqual(letra_dni("12345678"), "Z")

if __name__ == '__main__':
    unittest.main()