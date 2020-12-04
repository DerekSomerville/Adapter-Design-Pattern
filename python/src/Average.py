from python.src.Rounding import Rounding
from python.src.RoundUp import RoundUp
from python.src.RoundDown import RoundDown

class Average():
    roundingMethod = RoundDown()

    def setRoundingMethod(self,roundingMethod):
        self.roundingMethod = roundingMethod

    def calculateAverage(self,numbersAsString):
        numbers = numbersAsString.split(",")
        count = len(numbers)
        total = 0
        for number in numbers:
            total += int(number)
        average = self.roundingMethod.round(total,count)
        return average

    def main(self):
        numbers = input("Please input numbers e.g. 12,23,34")
        average = self.calculateAverage(numbers)
        print(average)

if __name__ == "__main__":
    average = Average()
    average.main()
