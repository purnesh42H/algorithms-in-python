import math

def is_prime(n):
    if n < 4:
        return True
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i  == 0:
            return False

    return True

def test_prime():
    assert is_prime(3) == True
    assert is_prime(11) == True
    assert is_prime(19) == True

test_prime()
