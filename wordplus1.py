word = input("what is the word?")
word1 = ''.join(chr(ord(letter)+1) for letter in word)
print(word1)
