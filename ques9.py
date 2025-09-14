number = int(input("enter a number:"))
number = abs(number)
digit_sum = 0
while number > 0:
    digit = number % 10
    digit_sum += digit
    number = number // 10
    print(f"sum of digits is: {digit_sum}")