class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_pick_up(self):
        print(f"You picked up the {self.name} \n {self.description}")

    def drop_item(self):
        print(f"You dropped {self.name}")

    def __repr__(self):
        return self.name


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories


class Egg(Food):
    def __init__(self):
        super().__init__("egg", "This is an egg", 50)
