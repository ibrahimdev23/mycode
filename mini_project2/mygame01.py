#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
   Welcome to the best  RPG Game!!!

   There are mulitple items hidden in Rooms throughout the map!
   To win you must find the hidden key and potion and make it to the Garden Room.
   But be careful to avoid the Monsters!
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""

    """Display a differnt status with more info if the player is in hidden room"""
    if currentRoom == 'Hidden Room':
        print('---------------------------')
        print('You are in the ' + currentRoom)
        #show the map the rooms that exists 
        message = """🎉🎉🎉  You have found the special hidden room!
        Type in the letter corresponding  to the room you want and
        you will be magically transported there! 🎉🎉🎉  """
        print(message)
        #player types in the letter that matches the room
        print("Pick: [D]ining Room, [L]iving Room, [B]asement, [G]arden, [K]itchen  ")
    else:
    # print the player's current location
        print('---------------------------')
        print('You are in the ' + currentRoom)
    # print what the player is carrying
        print('Inventory:', inventory)
    
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

#a list that will count how many moves the player has made
movesCounter = []




# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'key',
                
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster',
                },

            'Dining Room' : {
                'west': 'Hall',
                'south': 'Garden',
                'east': 'Living Room',
                'item': 'potion',
                },
            'Garden': {
                'north': 'Dining Room',
                },

            # 4 new rooms are added below 
            'Living Room': {
                'west': 'Dining Room',
                'south': 'Basement',
                'item': 'monster',
                },

            'Basement': {
                'north': 'Living Room',
                'east': 'Hidden Room',
                'west':'Bed Room'

                },
            'Hidden Room':{
                'west': 'Basement',
                },
            'Bed Room': {
                'west': 'Basement',
                'item': 'monster'
                }
            }

# start the player in the Hall
currentRoom = 'Hall'


#livesCount starts at 3 but goes down by 1 everytime a monster is encountered
livesCount = 3
showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    

    

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')


#when a player finds the hidden room, they can choose to go to any room directly
#the user inputs a letter matching the first letter of the room name
#a switch statment changes the current room according to input
    if currentRoom == 'Hidden Room': 
        match move.upper():
            case "L":
                currentRoom = 'Living Room'
            case "D":
                currentRoom = 'Dining Room'
            case "B":
                currentRoom = 'Basement'
            case "G":
                currentRoom = 'Garden'
            case "K":
                currentRoom = 'Kitchen'
            case "H":
                currentRoom = 'Hidden Room'
            case _:
                print("Pick a valid option: [L]iving Room, [D]ining Room, [B]asement, [G]arden, [K]itchen")
         


    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # the valid move gets added to the movesCounter list to track moves
            movesCounter.append(move)
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #any time a valid move is made it gets added to the movesCounter list
            movesCounter.append(move)

            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')



    #This function is only called when a player finds the special hidden room


    ## If a player enters a room with a monster
    # player has 3 lives.. an encounter with a monster decreases the player's lives by 1 
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        livesCount = livesCount - 1
        print('A monster has got you.. you have ' + str( livesCount) + ' lives left')
    if livesCount == 0:
        print('A monster has got you... and you have no more lives left.  GAME OVER!')  
        break

 ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        #the amount of moves made gets saved into a variable and then printed out
        moves = len(movesCounter)
        print('You made ' + str(moves) + ' moves to  win the game')
        print('=================================================================')
        break
