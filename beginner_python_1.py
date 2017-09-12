
def is_prime(number):
    """
    Determine whether a number is a primary number or not.

    Args:
        number: The number to be evaluated.

    Returns:
        Returns True if the input is a primary number, or False if it is not.

    Raises:
        TypeError: If the input is not of type integer
        ValueError: If the input is not greater than or equal to 2
    """
    if (type(number) != int):
        print("TypeError: Invalid Input. Please enter an integer larger than 1")
    elif (number < 2 ):
        print("ValueError: Invalid input. Please enter an integer larger than 1")        
    else:
        is_it_prime = True    
        for idx in range(2,number):
            if (number % idx == 0):
                is_it_prime = False
        return is_it_prime
