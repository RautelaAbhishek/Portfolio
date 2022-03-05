import os
import random

    # Clear Screen


    # Assignments
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cont = True
end = False
play = True

    # Functions
def deal():
    """Deals a random card"""
    return random.choice(cards)

def calculate(hand):
    value = sum(hand)
    if value == 21:
        return 0
    if 11 in hand:
        if value > 21:
            
            hand.remove(11)
            hand.append(1)
            value -= 10
    return value 

    

def drawCheck(player='user',end=False):
    bust = False
    print(f"\nUser Cards: {user_cards}         Dealer Cards: {dealer_cards}\n\nUser Score: {user_value}              Dealer Score: {dealer_value}")
    if user_value == 0:
        print(f"\n  Blackjack. You Win.")
        return True
    elif dealer_value == 0:
        print("\n   BlackJack. The dealer wins.")
        return True
    
    if user_value > 21:
        print("\n   Bust. The dealer wins.")
        bust = True
    elif dealer_value > 21:
        print("\n   The Dealer went bust. You Win")
    elif user_value > dealer_value and end == True:
        print("\n   You scored higher than the dealer. You Win.")
    elif dealer_value > user_value and end ==True:
        print("\n   The dealer scored higher than you. The dealer wins.")
    elif dealer_value == user_value and end ==True:
        print("You both have the same score. It\'s a draw.")
    
    if end == False and player == 'user' and bust == False:
        insert = input("\n    Do you want to draw another card?")
        if insert == 'n':
            return True
        elif insert == 'y':
            return False
    elif bust == True:
        return True
    
def playAgain():
    insert = input("\nWould you like to play again? ")
    if insert == 'y':
        return True
    else:
        quit()
while play == True:
    os.system('clear')
    print(logo)
    user_cards = []
    dealer_cards = []

    # Deal staring cards to User
    user_cards.append(deal())
    user_cards.append(deal())

    # Deal starting cards to Dealer
    dealer_cards.append(deal())
    dealer_cards.append(deal()) 

    # Test for blackjack
    user_value = calculate(user_cards)
    dealer_value = calculate(dealer_cards)
    cont = drawCheck()
    while cont == False:
        user_cards.append(deal())
        user_value = calculate(user_cards)
        cont = drawCheck()
    if user_value ==0:
        continue
    elif dealer_value == 0:
        drawCheck()
        continue
    elif user_value > 21:
        playAgain()
        continue
    else:
        while dealer_value < 17 and dealer_value != 0:
            dealer_cards.append(deal())
            dealer_value = calculate(dealer_cards)
    drawCheck(end=True)
        
    play = playAgain()