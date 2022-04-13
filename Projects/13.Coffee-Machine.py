import os


def collect_money(cost):
    print(f'The cost of your drink is ${"{0:.2f}".format(cost)}. Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))
    money = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    change = (money - cost)
    if change < 0 :
        print('Sorry thats not enough money. Money Refunded')
        collect_money(cost)
    
    return print(f'Here is $' +"{0:.2f}".format(change)+ ' in change.')



os.system('cls')



espresso_cost = 1.50
latte_cost = 2.50
coffee_cost = 3

water = 300
milk = 200
coffee = 100
money = 0

while True:
    apologise = 'Sorry there is not enough of the following'

    drink = input(f"What would you like (Espresso/Latte/Coffee)\n").lower()

    if drink == 'report':
        print(f'\nWater:  {water}ml \nMilk:   {milk}ml \nCoffee: {coffee}g \nMoney:  ${"{0:.2f}".format(money)}\n')
    elif drink == 'off':
        break
    elif drink == 'espresso':
        if water >= 50 and coffee >= 18:
            collect_money(espresso_cost)
            water -= 50
            coffee -= 18
            money += espresso_cost
            print(f"Here is your Espresso.\n")
        else:
            if water < 50:
                apologise += '\n- water'
            if coffee < 18:
                apologise += '\n- coffee'
            print(apologise)
    elif drink == 'latte':
        if water >= 200 and coffee >= 24 and milk >= 150:
            collect_money(latte_cost)
            water -= 200
            coffee -= 24
            milk -= 150
            money += latte_cost
            print("Here is your Latte.\n")
        else:
            if water < 200:
                apologise += '\n- water'
            if coffee < 24:
                apologise += '\n- coffee'
            if milk < 150:
                apologise += '\n- milk'
            print(apologise)
    elif drink == 'coffee':
        if water >= 250 and coffee >= 24 and milk >= 100:
            collect_money(coffee_cost)
            water -= 250
            coffee -= 24
            milk -= 100
            money += coffee_cost
            print("Here is your Coffee.\n")
        else:
            if water < 250:
                apologise += '\n- water'
            if coffee < 24:
                apologise += '\n- coffee'
            if milk < 100:
                apologise += '\n- milk'
            print(apologise)

        


