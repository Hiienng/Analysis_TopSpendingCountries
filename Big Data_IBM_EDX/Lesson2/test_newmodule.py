import unittest

from newmodule import area_of_circle

class TestCircle(unittest.TestCase):
    def test1(self):
        self.assertEqual(area_of_circle(2), 12.56)

unittest.main()