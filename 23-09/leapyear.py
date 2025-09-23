startyear = int(input("Enter the starting year: "))
endyear = int(input("Enter the end year: "))


for i in range(startyear-1,endyear+1):
    if((i%4 == 0 and i%100!= 0) or i%400 ==0):
        print(i)
