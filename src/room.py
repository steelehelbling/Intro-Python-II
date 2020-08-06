# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name=None, description=None, room_inventory=None,room_dangers=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.room_inventory = []
        self.room_dangers = []

    def __str__(self):
        return f'room: {self.name}, description: {self.description}'

    def get_item(self, item_name):
        for item in self.room_inventory:
            if item.name == item_name:
                return item
        else:
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
# class monster:
#     def __init__(self, name, description, dps):
#         self.name = name
#         self.description = description
#         self.dps = dps
#     def __repr__(self):
#         return f"{self.name}"
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"{self.name}"

# class Sharp(Item):
#     def __init__(self, name, description, dps):
#         super().__init__(name, description)
#         self.dps = dps