#!/usr/bin/env python
# coding: utf-8

# In[140]:


import random

def rock_paper_scissors():
       
##Keep tally of wins; best two out of three
    game = True    
    player_wins = 0
    ai_wins = 0
        
    ##Input Rock, Paper or Scissors
    while game == True:
        player_input = input("Please pick rock, paper, or scissors: ").lower()

        while player_input not in ('rock','paper','scissors'):
            print("Nope, pick rock, paper or scissors dumb dumb")
            player_input = input("Please pick rock, paper, or scissors: ")
            continue

        ## Computer randomly picks

        ai_input = random.choice(['rock','paper','scissors'])

        ## Figure out if player wins

        if (player_input == 'rock' and ai_input == 'scissors') or (player_input == 'paper' and ai_input == 'rock') or (player_input == 'scissors' and ai_input == 'paper'):
            print("Player wins")
            player_wins = player_wins + 1
            print("Score is Player: {} AI: {}".format(player_wins, ai_wins))


        ## Figure out if AI wins

        if (ai_input == 'rock' and player_input == 'scissors') or (ai_input == 'paper' and player_input == 'rock') or (ai_input == 'scissors' and player_input == 'paper'):
            print("AI wins")
            ai_wins = ai_wins + 1
            print("Score is Player: {} AI: {}".format(player_wins, ai_wins))
            
        ## Figure out if it's a draw

        if player_input == ai_input:
                print('TIE')

        ## Tally score

        if player_wins == 2 or (player_wins == 2 and ai_wins == 1):
                return 'PLAYER WINS!!!'
                game = False

        if ai_wins == 2 or (ai_wins == 2 and player_wins == 1):
                return "AI WINS OH GOD IT'S THE REVOLUTION!!!"
                game = False
