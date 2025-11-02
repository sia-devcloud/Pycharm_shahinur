def is_divisible_by(number, factor):
    """
    This function checks if a number is divisible by the given factor.
    :param number: number to check
    :param factor: factor to check
    :return: true or false
    """
    return number % factor == 0
def is_prime(number):
    is_prime_number = True
    if number < 2:
        is_prime_number = False
    for index in range(2,(number//2)+1):
        if is_divisible_by(number, index):
            is_prime_number = False
            break
    return is_prime_number

