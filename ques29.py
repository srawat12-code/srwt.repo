def longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
sentence = input("enter a sentence: ")
print(" the longest word is:",
    longest_word(sentence))
