def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))
my_list = [1,2,3,4,4,5,6,6,7,8]
print("original list:", my_list)
print("list without duplicates:", remove_duplicates(my_list))