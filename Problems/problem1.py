from utils import numeric

class Problem1:
    def __init__(self, multiple_1 = 3, multiple_2 = 5, maximum = 1000):
        """
        Our class Problem will take three inputs
        :param multiple_1:
        :param multiple_2:
        :param maximum:
        """
        self.multiple_1 = multiple_1
        self.multiple_2 = multiple_2
        self.maximum = maximum
    def compute(self):
        """
        This method will compute problem 1 of Euler's method
        :print: print the result
        """
        result = 0
        for index in range(1000):
            if numeric.is_divisible_by(index, self.multiple_1) or numeric.is_divisible_by(index, self.multiple_2):
                result = result + index
        print(f"Result of problem 1 of Euler's method is {result}")

