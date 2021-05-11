#Vars and Imports

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

########################################################################################################################
#Card Class:
#Suit, Rank, Value

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

########################################################################################################################

#Deck Class:
#Create all 52 Card objects
#Hold as a list of Card objects
#Shuffle a Deck through a method call
#Deal cards from the Deck object

#Deck class holds a list of card objects
#This means the Deck class will return Card class object instances,
#not just normal python data types.

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #Create the Card Object with every suit/rank
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

########################################################################################################################

#Player:
#Hold a players hand, add or remove cards from that hand
class Player:
    
    def __init__(self, name,):
        
        self.name = name
        self.all_cards = []
         
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            #list of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            #for a single Card object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} had {len(self.all_cards)} cards.'

########################################################################################################################
#Game Setup
    #Game Vars
player1 = Player('ONE')
player2 = Player('TWO')
new_deck = Deck()
new_deck.shuffle()
game_on = True
roundnum = 0

for x in range(26): #Zero is optional range(0, 26)
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())
    
#While game_on
while game_on:
    
    at_war = True
    roundnum += 1

    if roundnum > 10000: #IS THE GAME EVER GOING TO END?
        print('THE GAME WAS A TIE\n(Game may have continued)')
        game_on = False
        break
    
    print(f'Currently on {roundnum}:')

    if len(player1.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break
    if len(player2.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break
    
    #Start a new round
    #player1.all_cards is total cards in player one's deck
    #player_one_cards is the cards player one has on the table

    player_one_cards = []
    player_one_cards.append(player1.remove_one())
    player_two_cards = []
    player_two_cards.append(player2.remove_one())
    
    #while at_war
    '''
    Assume that war is true and if it's not true break out of the loop
    Personally I wouldn't code it this way but I'm doing this as a 100% code along and this is how he does it
    '''
    print(f'\t{player_one_cards[-1]} v.s. {player_two_cards[-1]}')

    if player_one_cards[-1].value > player_two_cards[-1].value:
        
        player1.add_cards(player_one_cards)
        player1.add_cards(player_two_cards)
        
    elif player_two_cards[-1].value > player_one_cards[-1].value:
        
        player2.add_cards(player_one_cards)
        player2.add_cards(player_two_cards)
        
    else:
        war_on = True
        print('WAR!')
        warvals = [player_one_cards[-1].value]
        spoils = []
        while war_on:
            if len(player1.all_cards) == 0: #game over check
                print('Player One unable to declare war\n Player Two wins')
                game_on = False
                war_on = False
                break
            elif len(player2.all_cards) == 0:#game over check
                print('Player Two unable to declare war\n Player One wins')
                game_on = False
                war_on = False
                break
            else: #War should happen
                spoils.append(player_one_cards[-1].value())
                spoils.append(player_two_cards[-1].value())
                print(spoils)
                if spoils[-2] in warvals: #Player One
                    player1.add_cards(spoils)
                    war_on = False
                    break
                if spoils[-1] in warvals: #Player Two
                    player2.add_cards(spoils)
                    war_on = False
                    break