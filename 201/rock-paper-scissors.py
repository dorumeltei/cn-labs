'''Instructions
take in a number 0-2 from the user that represents their hand
generate a random number 0-2 to use for the computer's hand
call the function get_hand to get the string representation of the user's hand
call the function get_hand to get the string representation of the computer's hand
call the function determine_winner to figure out who won
print out the player hand and computer hand
print out the winner
Some Tips:
Creating a function that gets a "hand" based on a number.

The function should take in a number and return the string representation of the hand. E.g.:

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper

    # for example if the variable hand is 0, it should return the string "scissor"
    pass'''

from random import randint

comp_hand = randint(0, 2)
user_hand = int(input('Chose hand (0 = rock, 1 = paper, 2 = scissors): '))
hand_lib = {0: 'rock', 1: 'paper', 2: 'scissors'}

def get_hand(comp, user):
    result = ''
    if hand_lib[comp] == hand_lib[user]:
        result = "It's a tie"
    elif hand_lib[comp] == 'rock':
        if hand_lib[user] == 'paper':
            result = 'User won'
        elif hand_lib[user] == 'scissors':
            result = 'Computer won'
    elif hand_lib[comp] == 'paper':
        if hand_lib[user] == 'scissors':
            result = 'User won'
        elif hand_lib[user] == 'rock':
            result = 'Computer won'    
    else:
        if hand_lib[user] == 'rock':
            result = 'User won'
        elif hand_lib[user] == 'paper':
            result = 'Computer won'

    return f'User chose {hand_lib[user]}; Computer chose {hand_lib[comp]}. {result}!'    

print(get_hand(comp_hand, user_hand))