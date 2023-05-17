from map import *
import random

class Character:

  def __init__(self, armor, damage):
    self.armor = armor
    self.damage = damage


class Player(Character):

  def armored(self, armor, damage):
    self.armor += armor
    self.damage += damage


def fight(actor1, actor2):
  actor1Win = actor1.armor / actor2.damage
  actor2Win = actor2.armor / actor1.damage

  if (actor1Win > actor2Win):
    return True

  else:
    return False

MainPlayerPower = Player(1, 1)
EricPower = Character(25, 30)
LittleDemonLegionPower = Character(15, 30)
EvilPower = Character(5, 5)

#Description about npc "Little Demon Legion", "Eric", and "Injured Old Man".
npcs = {
  "Little Demon Legion": {
    "Description": "Disgusting things, but it" +
    " seems that I need some more lethal weapons to defeat them.",
    "Location": [3, random.randrange(0,4)],
    "Action": ["fight", "leave"],
    "fight": "You fight with them.",
    "status": True,
    "Power": LittleDemonLegionPower
  },
  "Eric": {
    "Description":
    "He has an evil energy, and that energy" + " continues to grow.",
    "Location": island_map.end_point,
    "Action": ["fight", "leave"],
    "fight": "You face pure evil directly.",
    "status": True,
    "Power": EricPower
  },
  "Evil Old Man": {
    "Description": "I can't believe there are" + " still living humans here.",
    "Location": [1, random.randrange(0,4)],
    "Action": ["fight", "leave"],
    "fight": "You fight with him.",
    "status": True,
    "Power": EvilPower
  }
}
