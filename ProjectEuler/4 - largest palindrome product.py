def first_attempt(test_range):
    # first attempt
    palindrome = {}
    for i in range(1, test_range):
        for j in range(1, test_range):
            numlist = [digit for digit in map(int, str(i * j))]
            if numlist == list(reversed(numlist)):
                palindrome[i * j] = (i, j)
    print(palindrome[max(palindrome)], max(palindrome))

def second_attempt(test_range):
    # second attempt
    max_palindrome = 0
    factors = (0, 0)
    for i in range(test_range, 0, -1):
        for j in range(i, 0, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if str(product) == str(product)[::-1]:
                max_palindrome = product
                factors = i ,j
    print(max_palindrome, *[i for i in factors])

# first_attempt(1000)
second_attempt(1000)