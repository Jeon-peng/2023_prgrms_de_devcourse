import unittest
from dex_2_hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):
    def test_decimal_to_hex(self):
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(16), "10")
        self.assertEqual(decimal_to_hex(31), "1F")
        self.assertEqual(decimal_to_hex(0), "0")
        self.assertEqual(decimal_to_hex(1023), "3FF")
        
    def test_decimal_to_hex_boundary(self):
        self.assertEqual(decimal_to_hex(15), "F")
        self.assertEqual(decimal_to_hex(4095), "FFF")
        
    def test_decimal_to_hex_negative(self):
        self.assertEqual(decimal_to_hex(-1), None)
        
    def test_decimal_to_hex_float(self):
        self.assertEqual(decimal_to_hex(3.14), None)
        
    def test_decimal_to_hex_string(self):
        self.assertEqual(decimal_to_hex("42"), None)

if __name__ == '__main__':
    unittest.main()