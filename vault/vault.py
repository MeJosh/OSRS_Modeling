from item import Item
from monster import Monster
from player import Player
from gear_set import GearSet

import temp_test_data
from constants import GEAR_STATS, GEAR_SLOTS

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
        # TEMPORARY - Not yet implemented
        if name == "Bow of Faerdhinen":
            return temp_test_data.BOW_OF_FAERDHINEN
        else:
            return None

if __name__ == "__main__":
    vault = Vault("")
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
    print(test_gear.getAccuracy())

