def count_vowels_constants(input_strings):
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in input_string if char in vowels)
    constant_count = sum(1 for char in input_string if char.isalpha() and char not in vowels)
    return vowel_count, constant_count
input_string = input("enter a string: ")
vowels, constants = count_vowels_constants(input_string)
print(f"vowels: {vowels}")
print(f"constants: {constants}")