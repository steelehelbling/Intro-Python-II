# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, local_place):
        self.name = name
        self.local_place = local_place
        self.inventory = []

    def __str__(self):
        return f'name: {self.name}, room:{self.local_place}'

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
        else:
            return None
    def add_to_inventory(self, typen):
        if len(typen) > 1:
            item = self.local_place.get_item(typen[1])
            if item == None:
                print("the room has no such item")
            else:
                self.local_place.room_inventory.remove(item)
                self.inventory.append(item)
        else:
            print("type a item")
    def remove_from_inventory(self, typen):
        if len(typen) > 1:
            item = self.get_item(typen[1])
            if item == None:
                print("the room has no such item")
            else:
                self.local_place.room_inventory.append(item)
                self.inventory.remove(item)
        else:
            print("type a item")

    def change_rooms(self, control):
        new_room = self.local_place.get_room(control)
        if new_room != None:
            self.local_place = new_room

        else:
            print("no rooms connected to this one")

