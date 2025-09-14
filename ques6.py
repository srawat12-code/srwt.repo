num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
if num1 > num2:
    print(f"the largest number is{num1}")
elif num2 > num1:
    print(f"the largest number is{num2}")
else:
    print("both numbers are equal")