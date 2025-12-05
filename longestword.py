sentence = "Python is a powerful programming language"
words = sentence.split()

longest = max(words, key=len)
print("Longest word:", longest)
