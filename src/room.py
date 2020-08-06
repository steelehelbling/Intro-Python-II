# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name=None, description=None, room_inventory=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.room_inventory = []

    def __str__(self):
        return f'room: {self.name}, description: {self.description}'

    def get_item(self, item_name):
        for item in self.room_inventory:
            if item.name == item_name:
                return item
        return None

    def get_room(self, control):
        if control == "n":
            return self.n_to
        elif control == "s":
            return self.s_to
        elif control == "e":
            return self.e_to
        elif control == "w":
            return self.w_to
        else:
            return None

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"{self.name}"
