import os

os.system('clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo + "\n"+"Welcome to the secret auction program.")
bidders = {}
multipleWinner = False
while True:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bidders[name] = bid
    cont = input("Are there more bidders? ").lower()
    if cont == "yes" or cont == 'y':
        os.system('clear')
        continue
    else:
        break
for i in bidders:
    highest = 0
    if bidders[i] > highest:
        bidder = i
        highest = bidders[i]
    elif bidders[i] < highest:
        continue
    else:
        bidder2 = i
        multipleWinner = True
if multipleWinner == True:
    print(f"{bidder} and {bidder2} have bid the same amount of ${highest}")
else:
    print(f"The highest bidder is {bidder} with a bid of ${highest}")

