# Aqsa Noreen
# 9/6/2023
# CS-462

from random import randint
#Strtegy:
# set up a win table
# for every player's total, dealer's car, ace, simulate 10000 blackjack games
# for each game, deal initial cards for the player and the dealer then let the player
# draw cards until they surpass or reach the pre-determine stick_val
# now we let the dealer draw cards until they have a total 17 or higher
# we then determine the winner of the game and finally update the win table
def get_total(list_of_cards): # total value of the cards in hand
    total = sum(list_of_cards)
    # if ace
    if total <= 11 and 11 in list_of_cards:
        return total + 10
    return total

def draw_card(): # draw a card from our infinite deck
    return randint(1, 11)

def has_ace(hand): # check if ace is present
    return 1 if 11 in hand else 0


def blackjack():
    win_table = {}
    for i in range(4, 22):
        for j in range(1, 12):
            for k in range(0, 2):
                win_table[(i, j, k)] = 0

    for item in win_table:  ## for each item, let's see how many times we win if we hold there.
        for i in range(10000):
        ## play a game.
            # what are the players truly holding
            player_hand = (randint(1, 11), randint(1, 11))
            dealer_hand = (randint(1, 11), randint(1, 11))
            # what is our current state?
            observation = (get_total(player_hand),
                           dealer_hand[0],
                           1 if player_hand[0] == 11 or player_hand[1] == 11 else 0)

            stick_val = item[0]

            # Player draw cards until stick_val is exceeded
            while get_total(player_hand) < stick_val:
                player_hand += (draw_card(),)

            if get_total(player_hand) > 21:  # Player busts
                continue

            # Dealer draw cards until they have total of 17 or more
            while get_total(dealer_hand) <= 16:
                dealer_hand += (draw_card(),)

            #check if dealer bust
            if get_total(dealer_hand) > 21:
                win_table[item] += 1
                continue
            # check Player wins
            if get_total(player_hand) > get_total(dealer_hand):
                win_table[item] += 1

    # print out the percentage of times we won holding in this state.
    for item in win_table.keys():
        print("%s: %f" % (item, win_table[item] / 10000))

blackjack()


# Any card between 1 and 11 can be drawn and their prob is 1/11
# while calculating the player's card if the total is less than or equal to 11 and if
# there is an ace then we treat it as 11 making the total to be total + 10
# we know that if the player's total is over 21, they lose
# if dealer's total = 21 then dealer busts
# if neither of them lose then the person with the higher card total win!
# calculation of our win %: (number of player wins for player's total, dealer's card, ace )/10000
# Reference: https://note.nkmk.me/en/python-tuple-single-empty/#:~:text=The%20reason%20you%20need%20a,a%20tuple%2C%20not%20the%20parentheses.