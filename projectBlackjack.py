import random  
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
cards= [1,2,3,4,5,6,7,8,9,10,10,10,10,11]  #Cards in a deck
dealerHand = []  #Dealer's hand
playerHand = []  #Player's hand

def startgame():
        print(logo)
        print("Welcome to Blackjack!")

def dealHands():  #Deal hands to player and dealer (2 cards each)
        dealerHand.append(hit())
        dealerHand.append(hit())
        playerHand.append(hit())
        playerHand.append(hit())

def hit():
        return random.choice(cards)  #Randomly hit a card

def showHand():
        print(f"Your cards: {playerHand}, current score: {sum(playerHand)}")  #Show player's hand
        print(f"Computer's first card: {dealerHand[0]}")  #Show dealer's first card

def checkBlackjack():
        if sum(playerHand) == 21:  #Normal blackjack
                print("Blackjack! You win!")
                return True
        elif 11 in dealerHand and 10 in dealerHand: #Dealer blackjack
                print("Dealer has blackjack! You lose!")
                return True 
        else:
                return False  #No blackjack, continue game

def checkBust():
        if sum(playerHand) > 21:  #Normal bust
                print("Bust! You lose!")
                return True
        else:
                return False  #No bust, continue game

def checkWin():
        if sum(dealerHand) > 21: #Dealer bust
                return True
        elif sum(dealerHand) > sum(playerHand):  #Dealer win
                return False
        elif sum(dealerHand) < sum(playerHand):  #Player win
                return True
        else:  #Tie
                return False

def ace():
        if 11 in playerHand and sum(playerHand) > 21:
                while True:
                        print("You have an ace worth 11. Do you want to use it as 1 instead? (y/n)")
                        decision = input().lower()
                        if decision == 'y':
                                playerHand.remove(11)
                                playerHand.append(1)
                                break
                        elif decision == 'n':
                                break
                        else:
                                print("Invalid input. Please enter 'y' or 'n'.")




def play():
        dealHands() #Deal hands
        showHand() #Show hands
# Player's turn
        while True:
                if checkBlackjack():  #Check for blackjack
                        break
                elif checkBust():  #Check for bust
                        break
                else:
                        print("Do you want to hit or stand? (h/s)") # Hit or stand
                        decision = input().lower()
                        if decision == "h": #Hit
                                playerHand.append(hit())
                                showHand()
                                ace()
                        elif decision == "s": #Stand
                                break
                        else:
                                print("Invalid input. Please enter h or s.") #Invalid input

# Dealer's turn
        while sum(dealerHand) < 17:
                dealerHand.append(hit())

# Show dealer's hand and determine winner
        print(f"Dealer's cards: {dealerHand}, current score: {sum(dealerHand)}")
        if checkWin():  #Check for win
                print("You win!")
        else:
                print("You lose!")


startgame() #Start game
play() #Play game
