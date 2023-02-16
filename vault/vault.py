import os.path
import json
from item import Item
from monster import Monster
from player import Player
from gear_set import GearSet

from constants import GEAR_STATS, GEAR_SLOTS

ITEM_DIR = "/items"

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

    def getPlayerTemplate(self, name) -> Player:
        # TEMPORARY - Not yet implemented
        return {
            "name": name,
        }
    
    def getItemByName(self, name) -> Item:
        filename = f"{name.replace(' ', '_').lower()}.json"
        filepath = f"{self.dirPath}{ITEM_DIR}/{filename}"
        if not os.path.isfile(filepath):
            print(f"[ERROR] Unable to find file {filepath}")
            return None

        with open(filepath, 'r') as file:
            item_data = json.load(file)
            return Item(item_data)

if __name__ == "__main__":
    vault = Vault("./data")
    test_item = vault.getItemByName("Bow of Faerdhinen")
    #assert(test_item.getBonus(GEAR_STATS.ATTACK_RANGE) == 128)
    #print(test_item)
    #for stat in GEAR_STATS:
    #    print(stat + ": " + str(test_item.getBonus(stat)))

    test_gear = GearSet()
    print(test_gear)
    print(test_gear.getAttackSpeed())
    print(test_gear.attack_type)
    test_gear.setItemInSlot(GEAR_SLOTS.WEAPON, test_item)
    print(test_gear)
    print(test_gear.getBonus(GEAR_STATS.ATTACK_RANGE))
    print(test_gear.getAttackSpeed())
    print(test_gear.attack_type)
    print(test_gear.getAttackBonus())
