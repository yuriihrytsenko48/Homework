
"""
Task 1

Make a program that has some sentence (a string) on input and
returns a dict containing all unique words as keys and the number
of occurrences as values.
"""

sentence = input("Enter your sentence to count words:\n").lower().strip()

chars = [i for i in sentence]

sentence = ""

for char in chars:
    if char.isalnum() or char.isspace():
        sentence += char

sentence = sentence.split()

words_count = {}

for word in sentence:
    if word in words_count:
        continue
    else:
        words_count[word] = sentence.count(word)

for i, j in words_count.items():
    print(i, j)
