import math

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def find_prime(nth_prime):
    count = 0
    last_prime = 1
    while count < nth_prime:
        last_prime += 1
        if is_prime(last_prime):
            count += 1
    return last_prime

print(find_prime(10001))