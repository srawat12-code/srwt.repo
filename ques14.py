string = input("enter a string: ")
string_lower = string.lower()
if string_lower == string_lower[::-1]:
    print("palindrome")
else:
    print("not palindrome")