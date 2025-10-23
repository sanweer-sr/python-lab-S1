sentence = input("Enter a sentence: ")
search_word = input("Enter a word to search: ")


words = sentence.split()
count = len(words)

found = search_word in words

print("Number of words:", count)
print(f"Word '{search_word}' found:", found)
