n = int(input("Enter Min of 4 digit number"))


def rev(m):
    
    if m<1000:
        print("Enter a value greater than 1000")
        return
    new = 0
    while m>0 :
        d = m % 10
        new = new * 10 + d
        m = m // 10
    return new


print(rev(n))




