print("----------------------Greatest of Three Numbers---------------------")
num1 = int(input("Enter first Number"))
num2 = int(input("Enter Second Number"))
num3 = int(input("Enter Third Number"))

if num1>=num2 and num1>=num3:
    print("Number "+str(num1)+" is Greatest")

elif num2>=num1 and num2>=num3:
    print("Number "+str(num2)+" is Greatest")

else:
    print("Number "+str(num3)+" is Greatest")
