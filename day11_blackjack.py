# Day 11: Capstone Project
import asciiArt
import random as r
# PROJECT: Blackjack
# prints your cards in a list
# prints dealer's open card
# input hit or stand
# print both hands
# print winner
# input another round

# mechanics and program requirements
# any hand amount above 21 is a bust
# A counts as 1 or 11
# your score = dealer score, house wins
# dealer must hit on < 17, must stand on >= 17
# assume an infinite deck, so no removal
f_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cardict = dict(zip(f_cards, cards))
outcomes = ["d_bust", "y_bust", "d_higher", "y_higher", "tie", "fiver", "d_fiver"]

def hand_score(hand):
    aces = 0
    score = 0
    for card in hand:
        score += cardict[card]
        if card == f_cards[0]:
            aces += 1
    while (score > 21) and (aces > 0):
        score -= 10
        aces -= 1
    return score

def hit_me(hand):
    new_hand = hand + [r.choice(f_cards)]
    print(new_hand)
    return new_hand

def blackjack():
    y_wins = 0
    d_wins = 0
    ties = 0
    another_game = False
    if input('Enter "y" if you are you ready to play a hand of blackjack:\n') == "y":
        another_game = True
    while another_game:
        print(asciiArt.homer)
        dealer_hand = [r.choice(f_cards), r.choice(f_cards)]
        your_hand = [r.choice(f_cards), r.choice(f_cards)]
        dealer_score = hand_score(dealer_hand)
        your_score = hand_score(your_hand)
        print(f"This is your hand: {your_hand}")
        print(f"This is the dealer hand: ['?', '{dealer_hand[1]}']")
        hit = True
        while your_score < 21 and hit:
            if len(your_hand) >= 5:
                hit = False
            else:
                hit = input('Enter "hit" if you want another card, enter anything else to stand\n') == "hit"
                if hit:
                    your_hand = hit_me(your_hand)
                    your_score = hand_score(your_hand)
        if your_score == 21:
            print("Blackjack!!")
        if your_score > 21:
            print("You bust!")
            d_wins += 1
        elif len(your_hand) >= 5:
            print("You built a hand of 5 cards without busting. You win!!")
            y_wins += 1
        else:
            while dealer_score < 17:
                print("Dealer hits")
                dealer_hand = hit_me(dealer_hand)
                dealer_score = hand_score(dealer_hand)
            if dealer_score == 21:
                print("Dealer gets Blackjack!!")
            if dealer_score > 21:
                print("Dealer busts! You win!")
                y_wins += 1
            else:
                if dealer_score > your_score:
                    print(f"Dealer's score of {dealer_score} beats your score of {your_score}")
                    d_wins += 1
                elif dealer_score < your_score:
                    print(f"Dealer's score of {dealer_score} loses to your score of {your_score}")
                    y_wins += 1
                else:
                    print(f"It's a tie! Both have {dealer_score}")
                    ties += 1
        print(f"Dealer wins: {d_wins}  Your wins: {y_wins}  Ties: {ties}")
        if input('Enter "y" if you want to play another hand:\n') == "y":
            another_game = True
        else:
            another_game = False

def auto_blackjack(stop_condition):
    y_wins = 0
    d_wins = 0
    ties = 0
    another_game = True
    while another_game:
        print(asciiArt.homer)
        dealer_hand = [r.choice(f_cards), r.choice(f_cards)]
        your_hand = [r.choice(f_cards), r.choice(f_cards)]
        dealer_score = hand_score(dealer_hand)
        your_score = hand_score(your_hand)
        print(f"This is your hand: {your_hand}")
        print(f"This is the dealer hand: ['?', '{dealer_hand[1]}']")
        hit = True
        while your_score < 21 and hit:
            if len(your_hand) >= 5:
                hit = False
            else:
                hit = your_score < 17
                if hit:
                    print("You hit")
                    your_hand = hit_me(your_hand)
                    your_score = hand_score(your_hand)
        if your_score == 21:
            print("Blackjack!!")
        if your_score > 21:
            print("You bust!")
            outcome = outcomes[1]
            d_wins += 1
        elif len(your_hand) >= 5:
            print("You built a hand of 5 cards without busting. You win!!")
            outcome = outcomes[5]
            y_wins += 1
        else:
            while (dealer_score < 17) and (len(dealer_hand) < 5):
                print("Dealer hits")
                dealer_hand = hit_me(dealer_hand)
                dealer_score = hand_score(dealer_hand)
            if dealer_score == 21:
                print("Dealer gets Blackjack!!")
            if dealer_score > 21:
                print("Dealer busts! You win!")
                outcome = outcomes[0]
                y_wins += 1
            elif len(dealer_hand) >= 5:
                print("Dealer built a hand of 5 cards without busting. Dealer wins!")
                outcome = outcomes[6]
                d_wins += 1
            else:
                if dealer_score > your_score:
                    print(f"Dealer's score of {dealer_score} beats your score of {your_score}")
                    outcome = outcomes[2]
                    d_wins += 1
                elif dealer_score < your_score:
                    print(f"Dealer's score of {dealer_score} loses to your score of {your_score}")
                    outcome = outcomes[3]
                    y_wins += 1
                else:
                    print(f"It's a tie! Both have {dealer_score}")
                    outcome = outcomes[4]
                    ties += 1
        print(f"Dealer wins: {d_wins}  Your wins: {y_wins}  Ties: {ties}")
        if outcome == stop_condition:
            another_game = False

# blackjack()
auto_blackjack(outcomes[5])
