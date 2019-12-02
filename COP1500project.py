"""
Produces the number of characters, words, and the count of each word in a
sentence entered by the user
__author__= "Zachary Gossett"
COP1500-project-1
"""
print("Hello, this program will calculate the number of characters, "
      "words,\nand count of each word of a sentence. Please enter a "
      "sentence,\nbut do not put any punctuation marks.")
project_python = dict()
print("Enter a sentence: ")
line_entered = input("")
sentence_entered = line_entered.split()
print("The number of characters in your sentence is:", len(line_entered))
print("The number of words in your sentence is:", len(sentence_entered))
for word in sentence_entered:
    project_python[word] = project_python.get(word, 0) + 1
print("The words and the number of each words in your sentence are:",
      project_python)
