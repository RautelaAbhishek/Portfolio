import os
os.system('clear')

logo ='''
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(logo)

def calculation(fNum, lNum, operation):
    if operation == "+":
        return fNum + lNum
    elif operation == "-":
        return fNum - lNum
    elif operation == "/":
        return fNum / lNum
    elif operation == "*":
        return fNum * lNum
newCalc = False
cont = True

while cont == True:
    if newCalc == False:
        first_number = float(input("What is the first number: "))
    operator = input("Pick an operation: ")
    second_number = float(input("What is the next number: "))

    result = float(calculation(first_number,second_number,operator))
    print(f"{first_number} {operator} {second_number} = {result}")
    option = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'x' to end the program: ")
    if option == "y":
        newCalc = True
        first_number = result
    elif option == 'n':
        newCalc = False
        os.system('clear')
        print(logo)
    elif option == 'x':
        cont = False

