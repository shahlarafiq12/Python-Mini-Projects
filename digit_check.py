#write a program to check if a number is a single digit number , 2-digit number and so on upt to 5 digit number
number = int(input("Enter the number here upto 5 digit number: "))
if number >=0 and number <=9:
    print("Its a single digit number")

elif number >=10 and number <=99:
    print("Its a double digit number")

elif number >=100 and number <=999:
    print("Its a Triple digit number")

elif number >=1000 and number <= 9999:
    print("Its a 4 digit number")

elif number >= 10000 and number <= 99999:
    print("Its a 5 digit number")

else:
    print("Its out of 5 digit number")

    print("Thank You")