def print_numbers_between(start, end):
    if start > end:
        start, end = end, start
    for num in range(start, end + 1):
        print(num)
        
start_num = int(input("enter start number: "))
end_num = int(input("enter end number: "))
print_numbers_between(start_num, end_num)