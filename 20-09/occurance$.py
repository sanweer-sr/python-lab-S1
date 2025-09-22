string = input("Enter the String: ")


temp = string[0]
new = string[0] + string[1:len(string)].replace(temp, "$") 

print(string)
print(new)
