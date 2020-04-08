# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Food
from room import Room
# import os


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.health = 100

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(
                self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            # os.system("clear")
            print("You cannot move in that direction")

    def show_inventory(self):
        print(f"Inventory:\n")
        for item in self.inventory:
            print(item.name)

    def pick_up_item(self, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)
        print(f"You picked up {item.name}")

    def drop_item(self, item):
        self.inventory.remove(item)
        self.current_room.items.append(item)
        print(f"You dropped {item.name}")

    def eat(self, food_item):
        if not isinstance(food_item, Food):
            print("You cannot eat that item")
        else:
            self.health += food_item.calories
            print(
                f"You eat the {food_item.name}. Your health is now {self.health}")
            self.inventory.remove(food_item)
