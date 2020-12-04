import unittest
from python.src.RoundUp import RoundUp
from python.src.RoundDown import RoundDown
from python.src.Average import Average

class TestAverage(unittest.TestCase):
    average = Average()

    def test_AverageUp(self):
        roundUp = RoundUp()
        self.average.setRoundingMethod(roundUp)
        self.assertEqual(4, self.average.calculateAverage("3,4,3,5"))

    def test_AverageDown(self):
        roundDown = RoundDown()
        self.average.setRoundingMethod(roundDown)
        self.assertEqual(3, self.average.calculateAverage("3,4,3,5"))

if __name__ == '__main__':
    unittest.main()
