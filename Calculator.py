def welcome():
    return '''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$   Welcome to Georgi Horozov Calculator   $
$        Please select an option           $
$                continue                  $
$                                          $
$                                          $
$          Author: Georgi Horozov          $
$           Sofia, Bulgaria 2023           $
$                                          $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'''


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2


print(welcome())

while True:
    choice = input("1. Add\n2. Substract\n3. Multiply\n4. Devide\n5. Exit\nEnter your choice: ")

    if choice == "5":
        print("Thank you for using Georgi Horozov Calculator")
        break
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == "1":
        print("The sum is: ", add(n1, n2), "\n")

    elif choice == "2":
        print("The substract is: ", substract(n1, n2), "\n")

    elif choice == "3":
        print("The multiply is: ", multiply(n1, n2), "\n")

    elif choice == "4":
        print("The devide is: ", devide(n1, n2), "\n")


    else:
        print("Wrong choice!!!")