from room import Room
from player import Player
from room import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


Acid = Item('Acid', 'As an action, you can splash the contents of this vial onto a creature within 5 feet of you or throw the vial up to 20 feet, shattering it on impact. In either case, make a ranged attack against a creature or object, treating the acid as an improvised weapon. On a hit, the target takes 2d6 acid damage.')
Alchemist = Item("Alchemist's Fire", "This sticky, adhesive fluid ignites when exposed to air. As an action, you can throw this flask up to 20 feet, shattering it on impact. Make a ranged attack against a creature or object, treating the alchemists fire as an improvised weapon. On a hit, the target takes 1d4 fire damage at the start of each of its turns. A creature can end this damage by using its action to make a DC 10 Dexterity check to extinguish the flames.")
Amber = Item("Amber", "A transparent watery gold to rich gold gemstone worth 100 gold pieces. ")
Arrows = Item("Arrows", "Arrows are used with a weapon that has the ammunition property to make a ranged attack. Each time you attack with the weapon, you expend one piece of ammunition. Drawing the ammunition from a quiver, case, or other container is part of the attack (you need a free hand to load a one-handed weapon). At the end of the battle, you can recover half your expended ammunition by taking a minute to search the battlefield.")
Backpack = Item("Backpack","A backpack is a leather pack carried on the back, typically with straps to secure it. A backpack can hold 1 cubic foot/ 30 pounds of gear.You can also strap items, such as a bedroll or a coil of rope, to the outside of a backpack.")
Bagpipes = Item("Bagpipes","If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use bagpipes as a spellcasting focus.")
Battleaxe = Item("Battleaxe","Proficiency with a battleaxe allows you to add your proficiency bonus to the attack roll for any attack you make with it.")
room["outside"].room_inventory.append(Acid)
room["foyer"].room_inventory.append(Battleaxe)
room["overlook"].room_inventory.append(Amber)
room["narrow"].room_inventory.append(Arrows)
room["overlook"].room_inventory.append(Acid)
room["foyer"].room_inventory.append(Backpack)
room["overlook"].room_inventory.append(Bagpipes)
room["narrow"].room_inventory.append(Battleaxe)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
steele = Player('steelehelbling', room['outside'])

while True:
    print(f'\nroom: {steele.local_place.name}')
    print(f'\ndescription: {steele.local_place.description}')
    print(f'\ninventory: {steele.inventory}')
    print(f"\nroom inventory: {steele.local_place.room_inventory}\n")

    control = input("player controls \n n, s is to move up and down  \n w, e overlook is to move right or left \n g, r to grab or remove make sure to type a item\n q is to quit\n\n")
    if control in ['n', 's', 'w', 'e']:
        print("You moved to new room")
        steele.change_rooms(control)
    elif control == 'q':
        break
    control = control.split(" ")
    if control[0] not in ["g", "r"]:
        pass 
    
    elif control[0] == 'g':
            item = steele.local_place.get_item(control[1])
            
            if item == None:
                print("the room has no such item")
            else:
                steele.local_place.room_inventory.remove(item)
                steele.inventory.append(item)
                
                print(f'\n inventory:  {steele.inventory}')
                print(f"\n room inventory: {steele.local_place.room_inventory}")


    elif control[0] == 'r':
        item = steele.get_item(control[1])
        if item == None:
            print("the room has no such item")
        else:
            steele.local_place.room_inventory.append(item)
            steele.inventory.remove(item)
            
            print(f'\n inventory:  {steele.inventory}')
            print(f"\n room inventory: {steele.local_place.room_inventory}")
    else:
        print("wrong input")
print('run "python adv.py" to play anther round')