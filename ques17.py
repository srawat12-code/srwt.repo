def print_multiplication_table(num):
    print(f"multiplication table of {num}:")
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
        
num = int(input("enter a number: "))
print_multiplication_table(num)