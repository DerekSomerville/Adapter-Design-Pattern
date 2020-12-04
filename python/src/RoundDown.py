import math
from python.src.Rounding import Rounding

class RoundDown(Rounding):

    def round(self,total,count):
        return math.floor(total/count)

if __name__ == "__main__":
    roundDown = RoundDown()
    print(roundDown.round(15,4))
