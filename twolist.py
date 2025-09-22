list1 = []
list2 = []

sum1 = 0
sum2 = 0

limit = int(input("Enter The Size of the list"))

for i in range(limit):
    num = int(input(f"Enter The {i+1} number"))
    list1.insert(len(list1),num)
    sum1=sum1+num
        
limit2 = int(input("Enter The Size of the Second list"))

for i in range(limit2):
    num = int(input(f"Enter The {i+1} number"))
    list2.insert(len(list1),num)
    sum2=sum2+num

if(limit==limit2):
    print("Both has same Length")

if(sum1==sum2):
    print("sum of both are same")

for i in range(limit):
    for j in range(limit2):
        if(list1[i]==list2[j]):
            print(list2[j])
        


