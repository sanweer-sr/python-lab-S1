
sqrside = int(input("Enter the length of side : "))

squarearea = lambda x: x*x

print(f"The area of square is :{squarearea(sqrside)}")


rectside = int(input("Enter the length of rectangle : "))
rectside2 = int(input("Enter the width of rectangle : "))

rectanglearea = lambda x,y: x*y

print(f"The area of rectangle is :{rectanglearea(rectside,rectside2)}")

triaside = int(input("Enter the base of triangle : "))
triaside2 = int(input("Enter the height of triangle : "))

trianglearea = lambda x,y: 0.5*x*y

print(f"The area of triangle is :{trianglearea(triaside,triaside2)}")
