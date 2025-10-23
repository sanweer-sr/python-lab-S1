strings = input("Enter the string to be check for vowels")
lists = []

for i in range(len(strings)):
    i = strings[i]
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        lists.insert(len(lists),i)

print(lists)
