import os.path
import json
from .item import Item
from .monster import Monster
from .player import Player
from .gearset import GearSet

from .constants import GEAR_STATS, GEAR_SLOTS, SKILL_TYPES, ENEMY_STATS

TEMPLATE_DIR = "/templates"
ITEM_DIR = "/items"
MONSTER_DIR = "/monsters"
PLAYER_DIR = "/players"

class Vault():
    def __init__(self, dirPath) -> None:
        self.dirPath = dirPath
        self.players = {}
        self.monsters = {}
        self.items = {}

    def getPlayerByName(self, name) -> Player:
        # TEMPORARY - Not yet implemented
        return {
            "name": name,
        }

    def getPlayerByTemplate(self, name) -> Player:
        filename = f"{name.replace(' ', '_').lower()}.json"
        filepath = f"{self.dirPath}{TEMPLATE_DIR}{PLAYER_DIR}/{filename}"
        if not os.path.isfile(filepath):
            print(f"[ERROR] Unable to find file {filepath}")
            return None

        with open(filepath, 'r') as file:
            item_data = json.load(file)
            return Player(item_data)
    
    def getItemByName(self, name) -> Item:
        filename = f"{name.replace(' ', '_').lower()}.json"
        filepath = f"{self.dirPath}{ITEM_DIR}/{filename}"
        if not os.path.isfile(filepath):
            print(f"[ERROR] Unable to find file {filepath}")
            return None

        with open(filepath, 'r') as file:
            item_data = json.load(file)
            return Item(item_data)

    def getMonsterByName(self, name) -> Monster:
        filename = f"{name.replace(' ', '_').lower()}.json"
        filepath = f"{self.dirPath}{MONSTER_DIR}/{filename}"
        if not os.path.isfile(filepath):
            print(f"[ERROR] Unable to find file {filepath}")
            return None

        with open(filepath, 'r') as file:
            item_data = json.load(file)
            return Monster(item_data)

if __name__ == "__main__":
    vault = Vault("./data")
    test_item = vault.getItemByName("Bow of Faerdhinen")
    #assert(test_item.getBonus(GEAR_STATS.ATTACK_RANGE) == 128)
    #print(test_item)
    #for stat in GEAR_STATS:
    #    print(stat + ": " + str(test_item.getBonus(stat)))

    '''test_gear = GearSet()
    print(test_gear)
    print(test_gear.getAttackSpeed())
    print(test_gear.attack_type)
    test_gear.setItemInSlot(GEAR_SLOTS.WEAPON, test_item)
    print(test_gear)
    print(test_gear.getBonus(GEAR_STATS.ATTACK_RANGE))
    print(test_gear.getAttackSpeed())
    print(test_gear.attack_type)
    print(test_gear.getAttackBonus())'''

    test_monster = vault.getMonsterByName("King Black Dragon")
    print(test_monster)
    print(test_monster.getAttackSpeed())
    print(test_monster.getAttributes())
    print(test_monster.getSkillLevel(SKILL_TYPES.HITPOINTS))
    print(test_monster.getBonus(ENEMY_STATS.RANGE_STRENGTH))
