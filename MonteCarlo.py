# Aqsa Noreen
# 9/6/2023
# CS-462

#Strategy:
# for each hold value between n-5 and n we simulate the game 1000000 times.
# then player 1 roll repeatedly, they stop rolling and hold when the score exceeds the curr
#hold value or surpass n
# if player 1 score exceed n they lose
# if player 1 do not exceed n, player 2 will start rolling
# they roll until they beat player 1 without going over n
# if player 2 exceeds n or cannot beat the player 1 score, then player 1 wins

from random import randint
import random
def monte_carlo_approach(n):
    win_table = {} # dictionary is initialized
    for i in range(n - 5, n + 1):
        win_table[i] = 0

    # for each hold value n-5 to n
    for hold in range(n - 5, n + 1):
        for i in range(1000000):
            player1score = 0
            # player 1 will roll until tehy exceed n or reach hold value
            while player1score < hold and player1score <= n:
                player1score += random.randint(1, 6)
            # if exceeds n, player 1 lose and next simulation is started
            if player1score > n:
                continue

            player2score = 0
            #player 2 roll until they exceed player 1 score or n
            while player2score <= player1score and player2score <= n:
                player2score += random.randint(1, 6)
            # we then check who won
            if player2score > n or player1score > player2score:
                win_table[hold] += 1
    # print probabilities
    for item in win_table.keys():
        print("%d: %f" % (item, win_table[item] / 1000000))


monte_carlo_approach(10)