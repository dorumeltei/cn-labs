'''101 - tasks
Ask the player for their name.
Display a message that greets them and introduces them to the game world.
Present them with a choice between two doors.
If they choose the left door, they'll see an empty room.
If they choose the right door, then they encounter a dragon.
In both cases, they have the option to return to the previous room or interact further.
When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
When encountering the dragon, they have the choice to fight it.
If they have the sword from the other room, then they will be able to defeat it and win the game.
If they don't have the sword, then they will be eaten by the dragon and lose the game.

201 - tasks
Save the user input options you allow e.g. in a set that you can check against when your user makes a choice.
Create an inventory for your player, where they can add and remove items.
Players should be able to collect items they find in rooms and add them to their inventory.
If they lose a fight against the dragon, then they should lose their inventory items.
Add more rooms to your game and allow your player to explore.

Some rooms can be empty, others can contain items, and yet others can contain an opponent.
Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.



Specifically, there are two new big concepts that you can incorporate into your CLI game project to make it better:

File Input/Output
Functions
When you're done, here are some broad suggestions to consider:

State: Write the state of your gameplay to a file at the end of a session. You could use it to keep track of your player's inventory across multiple instances of your game.
Functions: Refactor your code to use functions for the different actions that your player can take. Then use your game loop to call the functions that the player chooses.
Documentation: Add docstrings and type hints to your functions. Explain what they do and learn to use good practices about writing readable and re-usable functions right from the start.
'''
import random, json
#test

objects_default = { 'name':'', 
            'lives': 3,
            'inventory':{'sword': 0, 'shield': 0, 'helmet': 0}}

try:
    with open('cli_game_conf.json', 'r') as file:
        objects = json.load(file)
except:
    with open('cli_game_conf.json', 'w') as file:
        objects = json.dump(objects_default, file, indent=4)
        objects = objects_default  

name = objects['name']
lives = objects['lives']

if name:
    name_ask = input(f'Hi. Is your name: {name}? anwer with Yes or No.')
    if name_ask.lower() == 'yes':
        print(f'Welcome back {name}. Let\'s continue the game')
    else:
        objects['name'] = input('What is your name? ')
else:
    objects['name'] = input('What is your name? ')
         
print(objects)
room = ''
partner_needed = random.choice([True, False])
print(f'Wecome {name} to Command Line Game!!')

def pick_objects(weapon):
    look_arround = input('Looking arround? Chose yes or no: ')
    if look_arround.lower() == 'yes':
        pick_up_sword = input(f'You find a {weapon}. Do you want to take it? Chose YES or NO: ')
        if pick_up_sword.lower() == 'yes': 
            objects['inventory'][weapon] += 1   
            print(F'{weapon} is taken')

def fight_opponent(opponent, weapon, partner = True):
    # global lives
    print(f'Here is a {opponent}')
    fight_opponent = input(f'Do you wish to fight the {opponent}? Chose YES or NO: ')
    if fight_opponent.lower() == 'yes':
        if objects['inventory'][weapon] >= 1 and partner == True:
            print(f'You have a {weapon}. {opponent} is defeated. You WIN!!!')
        else:
            if partner == False:
                no_partner_msg = ' and you have no parner to help you'
            else:
                no_partner_msg = ''
            objects['lives'] -= 1
            if objects['lives'] != 0:
                print(f'You don\'t have a {weapon}{no_partner_msg}. You lost a life. {lives} left!')
                for values in objects['inventory']:
                    objects['inventory'][values] = 0
            else:
                print('O lives left. You LOST the game.')

while objects['lives'] > 0:
    room = input('Chose a room. Options: blue, black, green, brown. Or quit the room game (exit). Your choice: ')
    if room == 'blue':
        print(f'You entered the {room} room.')
        chosen_door = input('Choose a door: left or right? ')
        if chosen_door.lower() == 'left':
            pick_objects('shield')
        elif chosen_door.lower() == 'right':
            pick_objects('helmet')

    elif room == 'black':
        print(f'You entered the {room} room. Room is empty!')
        chosen_door = input('Choose a door: left or right? ')
        if chosen_door.lower() == 'left':
            pick_objects('sword')              
        elif chosen_door.lower() == 'right':
            fight_opponent('dragon', 'sword')
        else:
            print('Please choose \'left\' or \'right\'')

    elif room == 'green':
        print(f'You entered the {room} room.')
        chosen_door = input('Choose a door: left or right? ')
        if chosen_door.lower() == 'left':
            pass
        elif chosen_door.lower() == 'right':
            print('partner needed: ', partner_needed)
            fight_opponent('monster', 'shield', partner_needed)

    elif room == 'brown':
        print(f'You entered the {room} room. Room is empty.')
    elif room == 'exit' or room == 'e':
        break

with open('cli_game_conf.json', 'w') as file:
        json.dump(objects, file, indent=4)   

print('Game over')

