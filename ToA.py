print "This game is complety fictional and any similarities to real life events are completely coincidentally" 

import sys 
#15 Nones for Rooms    
directions = ('n', 'e', 's', 'w', 'up', 'down', 'left', 'right', 'north', 'east', 'south', 'west')
node = None
class room():
    def __init__ (self, name, n, e, s, w, north, east, south, west, up, down, left, right,description, take):
        self.name = name 
        self.description = description
        self.n = n
        self.e = e
        self.s = s
        self.w = w
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.north = north
        self.east = east
        self.south = south 
        self.west = west
        self.take = take
    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]  
class inventory(object):
    def __init__(self, name, quantity):
        self.name = name
        self. quantity
        
def pickup(self):
    print "The item has been added to your inventory"
    append.item(inventory)

#IWasRIght
class Item(object):
    def __init__(self, name, quantity = 1):
        self.name = name.strip().lower()
        self.quantity = quantity
class Key(Item):
    def __init__(self,name, quantity = 1):
        self.name = name.strip().lower()
        
    def pickup(self):
        print "You have picked up %d", self.name
        ########################################
                
        
room1 = room('The Haze', 'DeskScroll', None, None, 'LockedDoor', 'DeskScroll', None, None, 'LockedDoor', None, None, None, None, None,'You awake atleast you think you are, all of you senses feel dulled and you feel a light hazy clouding your thoughts. As you get up you look around and you see a paper on sitting on a desk to the north. The room is a dark mahogany color that enshroud you in a blanket of warmth. A door is to the west of you.' )
DeskScroll = room('Instructions From Above', None, None, None, 'LockedDoor', None, None, None, 'LockedDoor', None, None, None, None, None,'The parchment reads from the top: THE TRIALS WILL TEST YOU PHYSICALLY AND SPRITUALLY, ONLY THE EXEMPLARY WILL COME OUT ALIVE. You see a key on the table.')  
LockedDoor = room('The Door', None, None, None, None, None, None, None, None, None, None, None, None, None, 'As you appoarch the only door in the room you notice the inctricat redesign of the wood carvings which display a beautiful goddess slaying a demon of some sort. It sends shivers down your spine and quickly draw your attention to the door handle. You reach to turn the knb but it is locked and it takes a key to open it. Do you have a key?')       

#if 'yes' in raw_input:
    #print'You put the key into the lock and the door cracks open.'
#else:
    #print'You need a key to open the door.'        
               
                             
node = room1
while True:
    print node.name
    print node.description
    movement = ["north", "south", "east", "west"]
    quit = ["q", "quit", "exit"]
    command = raw_input("Where to now? ")
    if command in quit:
        sys.exit(0)
    if command in movement:
        try:
            node.move(command)
        except:
            print "You can't move that way"
