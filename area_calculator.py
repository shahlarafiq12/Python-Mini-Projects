#write a program to create Area Calculator

print("**Area Calculator**")
print("""Press 1 to get a square calculator
Press 2 to get a Rectangle
Press 3 to get a Circle
Press 4 to get a Triangle""")


choice = int(input("Enter a number between 1-4: "))

if choice == 1:
    a = float(input("Enter the length of one side: "))
    a = a**2
    print("The area of square: ", a)

elif choice == 2:
    length = float(input("Enter the length of rectabgle: "))
    width = float(input("Enter the width of rectangle: "))
    area = length*width
    print("The area of rectangle:", area)

elif choice == 3:
    radius = float(input("Enter the radius of circle: "))
    area = 3.14*(radius**2)
    print("The area of circle: ", area)

elif choice == 4:
    base = float(input("Enter the base of triangle: "))
    height = float(input("Enter the height ot triangle: "))
    area = 0.5*base*height
    print("The area of circle: ", area)

else:
    print("Invalid number (PLease enter number between 1-4")