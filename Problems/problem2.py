from utils import numeric

class Problem2:
    def __init__(self,maximum = 4000000):
        self.maximum = maximum
    """
    This function will solve the problem 2 of Euler's 
    """
    def compute(self):
        first = 1
        second = 2
        result = 2
        while first + second < self.maximum:
            temp = first + second
            if numeric.is_divisible_by(temp, 2):
                result = result + temp
            first = second
            second = temp
        print(f"Result of the problem 2 of Euler's problem is {result}")