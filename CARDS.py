import random


class Cards:
    def __init__(self, rank, suit, face_up, value):
        self.suit = suit
        self.rank = rank
        self.face_up = face_up
        self.value = value


list_cards = []  # list to hold 52 cards
list_rank = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
list_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
face_up = True
players_hand = []
dealers_hand = []


# Builds deck of card 1 suit at a time
def build_deck_cards(list_rank, suit, face_up, value):
    for x in range(13):
        list_cards.append(Cards(list_rank[x], suit, face_up, list_value[x]))


def shuffle_deck(list_cards):
    random.shuffle(list_cards)


def deal(list_cards, hand):
    hand.append(list_cards.pop(0))


def sum_of_cards(hand):
    sum = 0
    for x in range(len(hand)):
        sum = sum + hand[x].value
    return sum


def show_players_hand(players_hand):
    print('\nPlayer has:')
    for x in players_hand:
        print("{} of {}".format(x.rank, x.suit))


def show_dealers_hand(dealers_hand):
    print('\nDealer has:')
    for x in dealers_hand:
        print("{} of {}".format(x.rank, x.suit))


suits_list = ['clubs', 'diamonds', 'hearts', 'spades']
for x in suits_list:
    build_deck_cards(list_rank, x, face_up, list_value)

shuffle_deck(list_cards)
deal(list_cards, dealers_hand)
deal(list_cards, dealers_hand)
deal(list_cards, players_hand)
deal(list_cards, players_hand)
show_players_hand(players_hand)
print("\nDealer has:")
for x in range(len(dealers_hand)):
    if x == 0:
        dealers_hand[x].face_up = False
        print("Card face down")
    else:
        print("{} of {}".format(dealers_hand[x].rank, dealers_hand[x].suit))
players_sum = sum_of_cards(players_hand)
print(players_sum)
dealers_sum = sum_of_cards(dealers_hand)
while players_sum < 21:
    if players_sum < 21:
        player_input = str(input("\nHit or Stay:")).upper()
    if player_input == 'HIT':
        deal(list_cards, players_hand)
        players_sum = sum_of_cards(players_hand)
        print(players_sum)
    if player_input == 'STAY':
        if players_sum < 21 and players_sum > dealers_sum:
            show_players_hand(players_hand)
            show_dealers_hand(dealers_hand)
            print('Player wins !!!')
            break
        elif players_sum < dealers_sum:
            show_players_hand(players_hand)
            show_dealers_hand(dealers_hand)
            print('Player loses !!!')

if players_sum > 21:
    print('Player bust!!')
    show_players_hand(players_hand)
    show_dealers_hand(dealers_hand)
if players_sum == 21:
    print('Player wins!!')
    show_players_hand(players_hand)
    show_dealers_hand(dealers_hand)








