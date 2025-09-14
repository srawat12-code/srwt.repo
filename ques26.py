def find_second_largest(list):
    if len(list) < 2:
        return None
    max_element = second_max = float('-inf')
    for num in list:
        if num > max_element:
            second_max = max_element
            max_element = num
        elif num > second_max and num !=max_element:
            second_max = num
    
    if second_max == float('-inf'):
        return None 
    return second_max
numbers = [12,34,54,2,3,54,1]
print("second largest element:", find_second_largest(numbers))