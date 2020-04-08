from room import Room
from player import Player
from item import Item, Food
# import os

# Declare all the rooms -> old example
# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }

# Make Rooms
outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")
foyer = Room(
    "Foyer", "Dim light filters in from the south. Dusty passages run north and east.")
overlook = Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.")
narrow = Room("Narrow Passage",
              "The narrow passage bends here from west to north. The smell of gold permeates the air.")
treasure = Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.")
treasure_east = Room(
    "Treasure East", "You've found the super secret treasure room")

# Link rooms together
# room['outside'].n_to = room['foyer'] -> old example
outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow
treasure.e_to = treasure_east
treasure_east.w_to = treasure

# Make Items
rock = Item("rock", "This is a rock")
sandwich = Food("sandwich", "This is a sandwich", 150)
coin = Item("coin", "Sweet, a coin!")

# Add Items to room
outside.items = [rock]
foyer.items = [sandwich]
treasure_east.items = [sandwich, coin]

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Enter your name: "), outside)
print(f"{player.current_room}")

# player.inventory.append(sandwich)

# Start Loop
directions = ("n", "s", "e", "w")
tools = ("i", "c", "t", "d")

while True:
    print(
        f"Available Tools: \n Show Inventory: '{tools[0]}' \n Take Items: '{tools[1]}' \n Drop Item: '{tools[2]}'")
    cmd = input("~~> ")
    if cmd == "q":
        print("Goodbye")
        exit(0)
    elif cmd in directions:
        player.travel(cmd)
    elif cmd == tools[0]:
        player.show_inventory()
    elif cmd == tools[1]:
        player.current_room.show_items()
    elif cmd == tools[2]:
        if len(player.current_room.items) == 0:
            print(f"THere are no items here")
        elif len(cmd) == 2:
            for item in player.current_room.items:
                if item.name == cmd[1]:
                    player.pick_up_item(item)
                elif item.name != cmd[1]:
                    print(f"ther is no {cmd[1]} in this room")
    elif cmd == tools[3]:
        pass
    else:
        print("That command does not work")
# End Loop


# longer/less DRY version
# LOOP
# while True:
#     # PRINT
#     print(f"Location: {player.current_room.name}")
#     print(player.current_room.description)
#     # READ
#     cmd = input("~~> ")
#     # EVALUATE
#     if cmd == "q":
#         print("Goodbye")
#         exit(0)
#     elif cmd == "n":
#         if player.current_room.n_to is not None:
#             player.current_room = player.current_room.n_to
#         else:
#             print("You cannot move in that direction")
#     elif cmd == "s":
#         if player.current_room.s_to is not None:
#             player.current_room = player.current_room.s_to
#         else:
#             print("You cannot move in that direction")
#     elif cmd == "e":
#         if player.current_room.e_to is not None:
#             player.current_room = player.current_room.e_to
#         else:
#             print("You cannot move in that direction")
#     elif cmd == "w":
#         if player.current_room.w_to is not None:
#             player.current_room = player.current_room.w_to
#         else:
#             print("You cannot move in that direction")
#     else:
#         print("That command does not work")
