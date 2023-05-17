import random

class object:
    def __init__(self, name, damage, armor):
        self.name = name
        self.damage = damage
        self.armor = armor

HolySword = object("HolySword", 20, 0)
HolyHelmet = object("HolyHelmet", 5, 10)
HolyArmor = object("HolyArmor", 5, 30)

#Description about objects "Holy Sword", "Holy Sword", and "Holy Armor".
objects = {
  "Holy Sword": {
    "Description": "You found a shining sword inserted" +
    " in a stone. That should be the Holy Sword.",
    "Location": [1, random.randrange(0,4)],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": HolySword
  },
  "Holy Helmet": {
    "Description":
    "You found a box, opened it, and" + " found a very beautiful helmet.",
    "Location": [2, random.randrange(0,4)],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": HolyHelmet
  },
  "Holy Armor": {
    "Description":
    "You notice that there seems to be" +
    " light in front of you, and after walking over, you find armor on" +
    " the scorched ground.",
    "Location": [3, random.randrange(0,4)],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": HolyArmor
  }
}
