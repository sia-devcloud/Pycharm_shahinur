from utils import numeric
from utils.numeric import is_divisible_by, is_prime


class Problem3:
    def __init__(self, number = 45000):
        self.number = number
        """
        This function is to solve the problem 3 of the Euler's Project
        """
    def compute(self):
        for index in range(self.number,1,-1):
            if is_divisible_by(self.number, index) and is_prime(index):
                print(f"Largest prime factor of {self.number} is {index}")
                break
