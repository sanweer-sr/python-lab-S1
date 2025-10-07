limit = int(input("Enter the maximum limit: "))
listnew=[]

for i in range(limit):
    if(i==0 or i==1):
        listnew.insert(i,1)
    else:
        listnew.insert(i,listnew[i-1]+listnew[i-2])
print(listnew)
