list1 =[1,4,8,5,6,9,7,4,5,8,5,4,5,15,4,7,88,96,25,1,4,11,23]
list2 =[]
i=0

while i<len(list1):
    if (list1[i]%2 ==0):
        new = list1.pop(i)
        list2.append(new)
    else:
        i=i+1

print(list1)
print(list2)
