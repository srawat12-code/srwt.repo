def are_anagrams(str1, str2):
    str1 = str1. replace(" ","").lower()
    str2 = str2. replace(" ","").lower()
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
str1 = input("enter first string: ")
str2 = input("enter second string: ")
if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")