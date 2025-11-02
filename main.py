from Problems.problem1 import Problem1
from Problems.problem2 import Problem2

def print_menu():
    print("""
    Welcome to Project Euler's Answers
    Right now problem 1, 2 is solved
    Which question would you like to solve?""")
    user_input = int(input("Enter your choice"))
    if user_input == 1:
        euler_problem = Problem1()
        euler_problem.compute()
    elif user_input == 2:
        euler_problem = Problem2()
        euler_problem.compute()


if __name__ == '__main__':
   print_menu()
