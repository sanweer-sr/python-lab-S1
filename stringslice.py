s= "Hello Welcome"
s1 = "C" + s[1:]
s2 =s.replace("Welcome","Hi")
print(s1)
print(s2)


strings = input("Enter the senetnce to check occurence of word")

splitstrings = strings.split()
print(splitstrings)

i=0
count =0

while (i<len(splitstrings)):
    
    j=0
    while (j<len(splitstrings)):
        if (splitstrings[i] == splitstrings[j]):
            
            count = count+1
        j=j+1
    print(f"{splitstrings[i]} - {count}")
    count =0
    i=i+1
    
