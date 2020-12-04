import math
from python.src.Rounding import Rounding

class RoundUp(Rounding):

    def round(self,total,count):
        return math.ceil(total/count)

if __name__ == "__main__":
    roundUp = RoundUp()
    print(roundUp.round(15,4))
