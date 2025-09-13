my_string = input("enter a string: ")
length = len(my_string)
if length % 2 == 1:
    middle_index = length // 2
    print("middle character:" , my_string[middle_index])
else:
    middle_index1 = length // 2-1
    middle_index2 = length // 2
    print("middle two characters:",
      my_string[middle_index1 :middle_index2+1])
      