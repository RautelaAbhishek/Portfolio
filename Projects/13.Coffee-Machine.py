import os


def collect_money(cost):
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))
    money = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    print(money)
    change = (money - cost)
    if change < 0 :
        print('Sorry thats not enough money. Money Refunded')
        collect_money(cost)
    
    return print(f'Here is $' +"{0:.2f}".format(change)+ ' in change.')



os.system('clear')

espresso_cost = 1.5
latte_cost = 2.5
coffee_cost = 3

water = 1000
milk = 1000
coffee = 1000
money = 0

while True:
    drink = input(f"What would you like (Espresso/Latte/Coffee)\n").lower()

    if drink == 'report':
        print(f'Water:  {water}ml \nMilk:   {milk}ml \nCoffee: {coffee}g \nMoney:  ${money}\n')
    elif drink == 'off':
        break
    elif drink == 'espresso':
        if water >= 50 and coffee >= 18:
            water -= 50
            coffee -= 18
    elif drink == 'latte':
        if water >= 200 and coffee >= 24 and milk >= 150:
            water -= 200
            coffee -= 24
            milk -= 150
    elif drink == 'coffee':
        if water >= 250 and coffee >= 24 and milk >= 100:
            collect_money(coffee_cost)
            water -= 250
            coffee -= 24
            milk -= 100
        if water < 250:
            print('Sorry there is not enough Water')
        if coffee < 24:
            print('Sorry there is not enough Coffee')
        if milk < 100:
            print('sorry there is not enough Milk')
            
        


