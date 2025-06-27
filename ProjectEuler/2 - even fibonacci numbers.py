total = 0
num1 = 0
num2 = 1
while (num1 + num2) < 4000000:
    num1, num2 = num2, num1 + num2
    if not num2 % 2:
        total += num2
print(total)