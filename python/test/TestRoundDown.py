import unittest
from python.src.RoundDown import RoundDown


class TestRoundUp(unittest.TestCase):
    roundingMethod = RoundDown()
    def test_round(self):
        self.assertEqual(3, self.roundingMethod.round(15,4))


if __name__ == '__main__':
    unittest.main()
