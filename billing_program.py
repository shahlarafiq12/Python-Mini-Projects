#write a program to create a billing system at supermarket

while True:
    name = input("Enter the customer name: ")
    total = 0

    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter the amount: "))
        quantity = int(input("Enter the quantity: "))
        total += amount*quantity
        repeat = input("Do you want to add more items? (Yes/No): ")
        if repeat == "no" or repeat == "No":
            break

    print("-"*40)
    print("Name: ", name)
    print("Items: ", quantity)
    print("-" * 40)
    print("Amount to be paid: ", total)
    print("-" * 40)

    repeat1 = input("Do you want add next customer? (Yes/No): ")
    if repeat1 == "no" or repeat1 == "No":
        break