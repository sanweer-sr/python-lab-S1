num = int(input("Enter the Mark to check passed"))

if num >= 40:
    print("Passed with " + str(num)+ " mark")
else:
    print("failed")




for x in range(6):
    y = int(input("Enter the "+ x +" sub mark"))
    if y >= 40:
        print("Passed with " + str(y)+ " mark")
    else:
        print("failed")
