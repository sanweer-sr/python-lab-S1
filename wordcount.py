
strings = input("Enter the senetnce to check occurence of word : ")

splitstrings = strings.split()
print(splitstrings)
i = 0

while i < len(splitstrings):
    count = 1
    j = i + 1
    while j < len(splitstrings):
        if splitstrings[i] == splitstrings[j]:
            splitstrings.pop(j)  
            count += 1
        else:
            j += 1  
    print(f"{splitstrings[i]} - {count}")
    i += 1     


    

