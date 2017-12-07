import math
import random
from is_prime_python import is_prime

def generate_prime(n=3):
    while True:
        p = random.randint(math.pow(2, n-2), math.pow(2, n-1) - 1)
        p = 2 * p + 1
        if is_prime(p):
            return p

print(generate_prime(8))
print(generate_prime(8))
print(generate_prime(8))
    
    
