limit = int(input("Enter The Size of the list"))
newlist =[]

for i in range(limit):
    num = int(input(f"Enter The {i+1} number"))
    if(num >= 100):
        newlist.insert(len(newlist),"over")
    else:
        newlist.insert(len(newlist),str(num))

print(newlist)
    
