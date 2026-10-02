import unittest
from main import to_upper

class Test(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(to_upper("Vaishali"), "VAISHALI")

unittest.main()