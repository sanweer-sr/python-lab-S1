option = 0


while option<5:
    print("--------------------MENU--------------------")
    print("Choose a option from 1-4")
    
    print("1. Occurance of the Words in sentance")
    print("2. Character Frequency in Word")
    print("3. Factors of given Number")
    print("4. Exit")
    
    option=int(input("Enter the Option: "))

    if option==1:
        strings = input("Enter the sentence to check occurrence of word: ")
        splitstrings = strings.split()
        word_count = {}
        for word in splitstrings:
            word_count[word] = word_count.get(word, 0) + 1
        for word, count in word_count.items():
            print(f"{word} - {count}")


    


    elif option == 2:
        strings = input("Enter the sentence to check occurrence of character: ")
        splitstrings = list(strings)
        print(splitstrings)
        i = 0

        while i < len(splitstrings):
            count = 1
            j = i + 1
            while j < len(splitstrings):
                if splitstrings[i] == splitstrings[j]:
                    splitstrings.pop(j)  # remove duplicate
                    count += 1
                else:
                    j += 1  # only increment if no pop, because pop shifts list left
            print(f"{splitstrings[i]} - {count}")
            i += 1      
        


    elif option == 3:
        n=int(input("Enter the number to check factors: "))
        result = []
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)
        print(result)
        

    elif option == 4:
        break
    
    else:
        print("Choose a option from 1-4")
        
print("MENU EXIT")
        
