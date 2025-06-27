def largest_prime_factor(n: int) -> int:
    last_factor = 1
    while n % 2 == 0:
        last_factor = 2
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            last_factor = p
            n //= p
        p += 2
    if n > 1:
        last_factor = n
    return last_factor

number = 600851475143
print(largest_prime_factor(number))
