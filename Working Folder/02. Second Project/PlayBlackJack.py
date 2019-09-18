import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card(object):
    """Create card with suit and value """

    def __init__(self, suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        self.deck =[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_components = ''
        for card in self:
            deck_components += '\n'+card.__str__()
        return 'The deck has: '+deck_components

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value >21 and self.aces:
            self.value -=10
            self.aces -=1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips will you bet?'))
        except ValueError:
            print('Enter a number')
        else:
            if chips.bet > chips.total:
                print("You can bet only",chips.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("whould you like to 'Hit' or 'Stand'? perss h or s")

        if x[0].lower() == 's':
            print("Player stands, dealer is playing")
            playing = False
        elif x[0].lower() == 'h':
            hit(deck,hand)
        else:
            print("Sorry, Try again !")
            continue
        break

def show_some(player,dealer):
    print("=============")
    print("\nDealer Hand is:")
    print("\n<<<Hidden Cards>>>")
    print('',dealer.cards[1])
    print("\nPlayer Hand is",*player.cards,sep='\n')
    print("\nPlayer hand value: ",player.value)
    print("=============")

def show_all(player,dealer):
    print("=============")
    print("\nDealer hand: ",*dealer.cards, sep='\n')
    print("Dealer hand Value : ",dealer.value)
    print("\nPlayer hand: ",*player.cards, sep='\n')
    print("Player hand vaue: ", player.value)
    print("=============")
def player_bust(player,dealer,chips):
    print("Player lose bet!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins Bet !")
    chips.win_bet()

def dealer_bust(player,dealer,chips):
    print("Dealer lose bet!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins bet!")
    chips.lose_bet()

def push(player,dealer):
    print("Player and Dealer are tied, its a Push!")


#Start  Playing Game

while True:

#create and shuffle deck
    deck = Deck()
    deck.shuffle()

#crate player and dealer hands
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
#crate player  chips
    player_chips = Chips()
    #dealer_chips = Chips()

#prompt player for bet

    take_bet(player_chips)

    #show the Cards

    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_bust(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <=21:

        while dealer_hand.value <= 17:

            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.ValueError:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player,dealer)
    new_game = input("Would you like to play again? 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing")
        break
