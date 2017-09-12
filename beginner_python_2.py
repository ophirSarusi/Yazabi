import beginner_python_1 as bp1

def return_primes(number):
    """
    Return all prime numbers smaller than the input number.

    Args:
        number: The number to be used as top limit.

    Returns:
        Returns an array of all prime numbers smaller than input number.

    Raises:
        TypeError: If the input is not of type integer
        ValueError: If the input is not greater than or equal to 2
    """
    primes_list = []    
    if (type(number) != int):
        print("TypeError: Invalid Input. Please enter an integer larger than 1")
    elif (number < 2 ):
        print("ValueError: Invalid input. Please enter an integer larger than 1")        
    else:
        for idx in range(2,number):
            if bp1.is_prime(idx):
                primes_list.append(idx)
        return primes_list
