def sum_using_loop(n):
    total = 0
    for i in range(1, n+ 1):
        total += i
    return total
n = int(input("enter a number: "))
print("sum using loop:", sum_using_loop(n))
        