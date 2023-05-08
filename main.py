#-----------------------------------------------------------------------------
#    File name: RPG - Try/Except
#    Author: Han Wang
#    Date created: 3/30/2023
#    Date last modified: 4/10/2023
#    version 1
#-----------------------------------------------------------------------------
'''   Description: Adventure Games'''
#-----------------------------------------------------------------------------
import map

#Create a variable "row" with a value of 0
row = 0
col = 0

#Create a list called inventory
inventory = [player]

playing = True

# tile information
#Create a list called tile
#The first assignment is "start", which means that tile[0] is "start",
#and so on
#Description about objects "Holy Sword", "Holy Sword", and "Holy Armor".
objects = {
  "Holy Sword": {
    "Description": "You found a shining sword inserted" +
    " in a stone. That should be the Holy Sword.",
    "Status": "in stone",
    "Location": [2, 1],
    "Action": ["take", "leave"],
    "Requirement": ["key", None, None]
  },
  "Holy Sword": {
    "Description":
    "You found a box, opened it, and" + " found a very beautiful helmet.",
    "Status": "in box",
    "Location": [0, 1],
    "Action": ["take", "leave"],
    "Requirement": [None, None]
  },
  "Holy Armor": {
    "Description":
    "You notice that there seems to be" +
    " light in front of you, and after walking over, you find armor on" +
    " the scorched ground.",
    "Status":
    "on ground",
    "Location": [3, 3],
    "Action": ["take", "leave"],
    "Requirement": [None, None]
  }
}

#Description about npc "Little Demon Legion", "Eric", and "Injured Old Man".
npcs = {
  "Little Demon Legion": {
    "Description": "Disgusting things, but it" +
    " seems that I need some more lethal weapons to defeat them.",
    "Status": "screaming",
    "Location": [4, 1],
    "Action": ["fight", "leave"],
    "Requirement": [None, None]
  },
  "Eric": {
    "Description":
    "He has an evil energy, and that energy" + " continues to grow.",
    "Status": "in sky",
    "Location": [4, 4],
    "Action": ["fight", "leave"],
    "Requirement": [None, None]
  },
  "Injured Old Man": {
    "Description": "I can't believe there are" + " still living humans here.",
    "Status": "in room",
    "Location": [2, 0],
    "Action": ["talk", "leave"],
    "Requirement": [None, None]
  }
}


# Functions ------------------------------------------------------------------
def walkto():
  global playing, row, col, max_row, max_col
  orientating = playing
  while orientating:
    print("Choose a direction: ")
    canUp = False
    canDown = False
    canRight = False
    canLeft = False

    if row > 0:
      canUp = True
      print("you can go up - type:'up'")

    if row < map.max_row:
      canDown = True
      print("you can go down - type:'down'")

    if col < map.max_col:
      canRight = True
      print("you can go right - type:'right'")

    if col > 0:
      canLeft = True
      print("you can go left - type:'left'")
    orientating = False

    #Create a variable called "waychoice" and assign it to user input
    #(input(f"Choice: ")), then change the user input to lowercase (.lower())
    waychoice = input("Choice: ").lower()
    if waychoice == "up" and canUp:
      row = row - 1

    elif waychoice == "down" and canDown:
      row = row + 1

    elif waychoice == "right" and canRight:
      col = col + 1

    elif waychoice == "left" and canLeft:
      col = col - 1
    elif waychoice == "quit":
      playing = False

    else:
      print("There's no road there, only the sea.")
      waychoice = True


def Inspectplace1():
  global row, col, inventory, objects
  found_object = False
  location_description = map.map[row][col]
  for object in objects:
    object_row = objects[object]["Location"][0]
    object_col = objects[object]["Location"][1]
    if object_row == row and object_col == col:
      print(f"{objects[object]['Description']}")


def Inspectnpc1():
  global row, col, inventory, npcs
  found_npc = False
  location_description = map.map[row][col]
  for npc in npcs:
    npc_row = npcs[npc]["Location"][0]
    npc_col = npcs[npc]["Location"][1]
    if npc_row == row and npc_col == col:
      print(f"{npcs[npc]['Description']}")


# try-except-else-finally statements-----------------------------------------
def MainMenu():
  global playing, objects
  orientating = playing
  while orientating:
    while True:
      #try statement
      try:
        print("Choose to move to another area or look around:")
        Choose = ["walk", "look", "quit"]
        i = 0
        for do in Choose:
          i = i + 1
          print((f"{i} - ({do.title()})"))
        userInput = int(input("You choice: "))
        orientating = False
        
      except ValueError:
        print("this is not a number")
        continue

      else:
        if userInput == 1:
          print("You went to the area ahead")
          walkto()
          
        elif userInput == 2:
          print("You look around.")
          #Function call
          Inspectplace1()
          Inspectnpc1()

        #if the user chooses to quit, the game quit
        elif userInput == 3:
          playing = False
          
        else:
          print("Invalid input!")
          orientating = True
        break
        
      finally:
        print("player still alive")
        

# Main ----------------------------------------------------------------------
# Open in read mode
file = open("story.txt", "r")
print(file.read())
file.close()

place = [
  "Start", "A swampy land", "A charred jungle", "Bloody Lake",
  "Demon Flower Field", "sacrificial altar", "broken church", "land of cracks"
]
max_length = len(max(place, key=len)) + 1

print(
  "+---------------------------------------------------------------------" +
  "--------------+")

for mapRow in map.map:
  for mapCol in mapRow:
    print("| {:{}}".format(mapCol, max_length), end="")
  print(
    "|\n+----------------------------------------------------------------" +
    "-------------------+")

while playing:
  location_description = map.map[row][col]
  for tile in map.tiles:
    if tile == location_description:
      print(map.tiles[tile]["Description"])

#class 
class player:
  def __init__(self, armor, damage)
  global inventory
  self.armor = armor
  self.damage = damage
  self.inventory = inventory

  MainPlayer = player(1, 1)

  Eric = player(4, 4)

  LittleDemonLegion = player(2, 2)
  

  MainMenu()
