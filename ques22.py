def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num

numbers_list = [12,7,45,23,56,89,34,19]
max_num, min_num = find_max_min(numbers_list)
print(f"maximum number: {max_num} ")
print(f"minimum number: {min_num} ")
