import random

marks = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Soldier', 'Queen', 'King']
deck_of_cards = [(i, j) for i in ranks for j in marks]

def hand_value(hand):
    value = 0
    number_of_Aces = sum(1 for card in hand if card[0] == 'Ace')

    for card in hand:
        if card[0] in ['Soldier', 'Queen', 'King']:
            value += 10
        elif card[0] == 'Ace':
            value += 11
        else:
            value += int(card[0])

    while value > 21 and number_of_Aces > 0:
        value -= 10
        number_of_Aces -= 1

    return value

def dealing_card():
    return deck_of_cards.pop(random.randint(0, len(deck_of_cards) - 1))

player_hand = [dealing_card(), dealing_card()]
dealer_hand = [dealing_card(), dealing_card()]

while True:
    print("Player's hand: ", player_hand)
    print("Dealer's hand: ", [dealer_hand[0], "?"])

    if hand_value(player_hand) == 21:
        print("Blackjack :)\nYou won")
        break
    elif hand_value(dealer_hand) == 21:
        print("You lost")
        break

    choice = input("type that you hit(h) or stand(s)? ").lower()

    if choice == 'h':
        player_hand.append(dealing_card())
        if hand_value(player_hand) > 21:
            print("You lost :(")
            break
    elif choice == 's':
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(dealing_card())

        print("Player's hand: ", player_hand, "Value: ", hand_value(player_hand))
        print("Dealer's hand: ", dealer_hand, "Value: ", hand_value(dealer_hand))

        player_value = hand_value(player_hand)
        dealer_value = hand_value(dealer_hand)

        if dealer_value > 21 or player_value > dealer_value:
            print("You Won")
        elif dealer_value > player_value:
            print("You Lost")
        else:
            print("This is tie")

        break

print("End of the game")