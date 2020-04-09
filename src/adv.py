from room import Room
from player import Player
from item import Item, Food
# import can also be done as follows:
#
# import room
# import player
# import item
#
# But if you use things from those file imports you would have to access it like and object. Ex: -> room_name = room.Room("name of room", "description")


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
#
# Could have also renamed the rooms as follows:
# outside = room['outside']


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


# Start Loop
directions = ("n", "s", "e", "w")
tools = ("i", "c", "t", "d", "eat", "q")

while True:
    print(
        f"Available Tools: \n Show Inventory: '{tools[0]}' \n Check for items: '{tools[1]}' \n Take Items: '{tools[2]} + item name' \n Drop Item: '{tools[3]} + item name' \n Eat: '{tools[4]} + item name' \n Quit: '{tools[5]}' \n")
    cmd = input("~~> ")
    multi_cmd = cmd.split(" ")
    if cmd == "q":
        print("Goodbye")
        exit(0)
    elif cmd in directions:
        player.travel(cmd)
    elif cmd == tools[0]:
        player.show_inventory()
    elif cmd == tools[1]:
        player.current_room.show_items()
    elif multi_cmd[0] == tools[2]:
        if len(player.current_room.items) == 0:
            print(f"There are no items here")
        elif len(multi_cmd) == 2:
            for item in player.current_room.items:
                if item.name == multi_cmd[1]:
                    player.pick_up_item(item)
                elif item.name != multi_cmd[1]:
                    print(f"ther is no {multi_cmd[1]} in this room")
    elif multi_cmd[0] == tools[3]:
        if len(player.inventory) == 0:
            print("Inventory is empty")
        elif len(multi_cmd) == 1 and multi_cmd[0] == tools[3]:
            print("Choose an item to drop")
        elif len(multi_cmd) == 2:
            for item in player.inventory:
                if item.name == multi_cmd[1]:
                    player.drop_item(item)
                elif item.name != multi_cmd[1]:
                    print(f"There is no {multi_cmd[1]} in your inventory")
    elif multi_cmd[0] == tools[4]:
        if len(player.inventory) == 0:
            print("Inventory is empty")
        elif len(multi_cmd) == 1 and multi_cmd[0] == tools[4]:
            print("Choose a food item to eat")
        elif len(multi_cmd) == 2:
            for item in player.inventory:
                if item.name == multi_cmd[1]:
                    player.eat(item)
                elif item.name != multi_cmd[1]:
                    print(f"There is no {multi_cmd[1]} in your inventory")

    else:
        print("That command does not work")
# End Loop
