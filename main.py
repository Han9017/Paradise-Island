#-----------------------------------------------------------------------------
#    File name: RPG - Try/Except
#    Author: Han Wang
#    Date created: 3/30/2023
#    Date last modified: 4/10/2023
#    version 1
#-----------------------------------------------------------------------------
'''   Description: Adventure Games'''
#-----------------------------------------------------------------------------
from map import *
from character import *
from item import *

#Create a variable "row" with a value of 0
row = start_point[0]
col = start_point[1]

#Create a list of NPCs

playing = True
inventory = []

# tile information
#Create a list called tile
#The first assignment is "start", which means that tile[0] is "start",
#and so on

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

    if row < island_map.max_row:
      canDown = True
      print("you can go down - type:'down'")

    if col < island_map.max_col:
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


#Here is the code where players can pick up items
def Inspectplace1():
  #Positioning items
  global row, col, inventory, objects
  InspectAction(objects)

#This is the code for different npcs on the map
def Inspectnpc1():
  #Positioning npcs
  global row, col, inventory, npcs
  InspectAction(npcs)

def InspectAction(objects):
  global row, col, inventory, playing
  for object in objects:
    object_row = objects[object]["Location"][0]
    object_col = objects[object]["Location"][1]
    object_status = objects[object]["status"]
    if object_row == row and object_col == col and object_status:
      #Description that will appear after finding the item
      print(f"{objects[object]['Description']}")
      Choose = objects[object]["Action"]
      for do in Choose:
        print((f"- {do.title()}"))
      #player input, can recognize player's capitalization
      userInput = input("You choice: ").lower()
      #Battle Code
      if userInput == Choose[0]:
        
        if Choose[0] == "take":
          currentItem = objects[object]["armor"]
          print(f"{objects[object]['Take']}")
          #Add items to the inventory
          inventory += currentItem.name
          MainPlayerPower.armored(currentItem.armor, currentItem.damage)
          objects[object]["status"] = False
          
        elif Choose[0] == "fight":
          print(f"{objects[object]['fight']}")
          if fight(MainPlayerPower, objects[object]['Power']):
            print("You Win!")
            objects[object]["status"] = False
            if end_point[0] == row and end_point[1] == col:
              print("You've saved the world! Nice Job!")
              playing = False
              
          elif not fight(MainPlayerPower, objects[object]['Power']):
            print("You lost! Try to get stronger!")

      elif userInput == Choose[1]:
        print("You leave")

      else:
        print("Invalid input!")
        

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
        print("Round ended")
        print("you are now at " + str(row) + ", " + str(col))


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

for mapRow in island_map.detail:
  for mapCol in mapRow:
    print("| {:{}}".format(mapCol, max_length), end="")
  print(
    "|\n+----------------------------------------------------------------" +
    "-------------------+")

while playing:
  location_description = island_map.detail[row][col]
  for tile in tiles:
    if tile == location_description:
      print(tiles[tile]["Description"])
  MainMenu()
