word = input("enter a word: ")
word_lower = word.lower()
if word_lower == word_lower[::-1]:
    print("palindrome")
else:
    print("not palindrome")
            