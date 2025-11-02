from Problems.problem1 import Problem1

def print_menu():
    print("""
    Welcome to Project Euler's Answers
    Right now problem 1 is solved
    Which question would you like to solve?""")
    user_input = int(input("Enter your choice"))
    if user_input == 1:
        euler_problem_1 = Problem1()
        euler_problem_1.compute()

if __name__ == '__main__':
   print_menu()
