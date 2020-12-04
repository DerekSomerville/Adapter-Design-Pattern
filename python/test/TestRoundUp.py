import unittest
from python.src.RoundUp import RoundUp


class TestRoundUp(unittest.TestCase):
    roundingMethod = RoundUp()
    def test_round(self):
        self.assertEqual(4, self.roundingMethod.round(15,4))


if __name__ == '__main__':
    unittest.main()
