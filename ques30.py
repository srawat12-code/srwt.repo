def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

    input_str = input("enter a string: ")
    print("reversed string:", reverse_string(input_str))