from math import factorial
import math

def too_slow_attempt():
    result = 0
    max_divisible = 20
    for i in range(1, factorial(max_divisible) + 1):
        if all([not(i % j) for j in range(1, max_divisible + 1)]):
            result = i
            break

    print(result)

def second_attempt(max_divisible):
    factors = []
    prime = [True for i in range(max_divisible + 1)]
    p = 2
    while p * p <= max_divisible:
        if prime[p]:
            for i in range(p * p, max_divisible + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, max_divisible + 1):
        if prime[p]:
            factors.append(p)
    result = 1
    for p in factors:
        e = int(math.log(max_divisible, p))
        result *= p**e
    print(result)

second_attempt(20)
