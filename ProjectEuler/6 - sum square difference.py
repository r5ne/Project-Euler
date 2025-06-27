def sum_square_diff(max_val: int) -> int:
    sum_of_squares = sum(i**2 for i in range(1, max_val + 1))
    square_of_sum = sum(i for i in range(1, max_val + 1))**2
    return square_of_sum - sum_of_squares

print(sum_square_diff(100))