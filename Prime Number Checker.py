def is_prime(number):
    """Check if a number is prime."""
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number < 2:
        return False

    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i = i + 1

    return True


print(is_prime(2))   # True
print(is_prime(5))   # True
print(is_prime(21))  # False
print(is_prime(2005))# False
print(is_prime(17))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
print(is_prime(0))   # False
