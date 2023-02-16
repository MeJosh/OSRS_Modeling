from calc import DPS
from player import Player
from enemy import NPC
from item import Item, ItemSet
import numpy as np
import unittest


#Test items
bowfa = Item(['Bow of faerdhinen', 0, 0, 0, 0, 128, 0, 0, 0, 0, 0, 0, 106, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0])
tbow = Item(['Twisted bow', 0, 0, 0, 0, 70, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0])
dhcb = Item(['Dragon hunter crossbow', 0, 0, 0, 0, 95, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0])
dhl = Item(['Dragon hunter lance', 85, 65, 65, 0, 0, 0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0])

keris = Item(['Keris partisan of breaching', 58, -2, 57, 0, 0, 0, 0, 0, 0, 0, 45, 0, 0, 3, 0, 0, 0, 0, 0, 4, 0, 0])

dragon_defender = Item(['Dragon defender', 25, 24, 23, -3, -2, 25, 24, 23, -3, -2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0])

crystal_body = Item(['Crystal body', 0, 0, 0, -18, 31, 46, 38, 48, 44, 68, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0])
crystal_helm = Item(['Crystal helm', 0, 0, 0, -10, 9, 12, 8, 14, 10, 18, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0])
crystal_legs = Item(['Crystal legs', 0, 0, 0, -12, 18, 26, 21, 30, 34, 38, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0])

inquis_body = Item(['Inquisitor\'s hauberk', 0, 0, 0, -18, 31, 46, 38, 48, 44, 68, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0])
inquis_legs = Item(['Inquisitor\'s plateskirt', 0, 0, 0, -10, 9, 12, 8, 14, 10, 18, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0])
inquis_helm = Item(['Inquisitor\'s great helm', 0, 0, 0, -12, 18, 26, 21, 30, 34, 38, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0])

elite_void_body = Item(['Void knight body', 0, 0, 0, 0, 0, 45, 45, 45, 45, 45, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0])
elite_void_robes = Item(['Void knight robes', 0, 0, 0, 0, 0, 30, 30, 30, 30, 30, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0])
void_gloves = Item(['Void knight gloves', 0, 0, 0, 0, 0, 6, 6, 6, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
void_helm_melee = Item(['Void melee helm', 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
void_helm_range = Item(['Void ranger helm', 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
void_helm_mage = Item(['Void mage helm', 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

salve_amulet_ei = Item(['Salve amulet', 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0])

#gearsets
#body, legs, ring, necklace, boots, ammo, helm, weapon, offhand, gloves, cape, attackStyle
crystal_with_bowfa = ItemSet(crystal_body, crystal_legs, None, None, None, None, crystal_helm, bowfa, None, None, None, ['Accurate', 'Ranged'])
crystal_with_tbow = ItemSet(crystal_body, crystal_legs, None, None, None, None, crystal_helm, tbow, None, None, None, ['Accurate', 'Ranged'])
void_with_bowfa = ItemSet(elite_void_body, elite_void_robes, None, None, None, None, void_helm_range, bowfa, None, void_gloves, None, ['Accurate', 'Ranged'])
void_with_tbow = ItemSet(elite_void_body, elite_void_robes, None, None, None, None, void_helm_range, tbow, None, void_gloves, None, ['Accurate', 'Ranged'])
ranged_void_with_lance = ItemSet(elite_void_body, elite_void_robes, None, None, None, None, void_helm_range, dhl, None, void_gloves, None, ['Controlled', 'Stab'])
melee_void_with_lance = ItemSet(elite_void_body, elite_void_robes, None, None, None, None, void_helm_melee, dhl, dragon_defender, void_gloves, None, ['Controlled', 'Stab'])
dhcb_with_salve = ItemSet(None, None, None, salve_amulet_ei, None, None, None, dhcb, dragon_defender, void_gloves, None, ['Accurate', 'Ranged'])
lance_with_defender =ItemSet(None, None, None, None, None, None, None, dhl, dragon_defender, void_gloves, None, ['Controlled', 'Stab'])
void_mage = ItemSet(elite_void_body, elite_void_robes, None, None, None, None, void_helm_mage, None, None, void_gloves, None, ['Accurate', 'Mage'])
void_mage_with_melee = ItemSet(elite_void_body, elite_void_robes, None, None, None, None, void_helm_mage, None, None, void_gloves, None, ['Controlled', 'Stab'])
inquis_crush = ItemSet(inquis_body, inquis_legs, None, None, None, None, inquis_helm, None, None, void_gloves, None, ['Controlled', 'Crush'])
inquis_notCrush = ItemSet(inquis_body, inquis_legs, None, None, None, None, inquis_helm, None, None, void_gloves, None, ['Controlled', 'Stab'])
partialInquis_crush = ItemSet(inquis_body, inquis_legs, None, None, None, None, None, keris, None, void_gloves, None, ['Controlled', 'Crush'])



#enemies
vorkath = NPC(['Vorkath', 0, 0, 0, 750, 560, 308, 214, 150, 308, 5, ['Slash', 'Mage', 'Ranged', 'Dragonfire'], 16, 0, 150, 56, 78, 0, 26, 108, 108, 240, 26, 0, ['Undead', 'Dragon'], 0, 0])
kq = NPC(['Kalphite queen', 0, 0, 0, 255, 300, 300, 300, 150, 1, 4, ['Stab', 'Ranged', 'Mage'], 0, 0, 0, 0, 0, 0, 50, 50, 10, 100, 100, 0, ['Kalphite'], 0, 0])

#Player
maxedPlayer = Player(99.0, 99.0, 99.0, 99.0, 99.0, 99.0, 99.0)

test = DPS(maxedPlayer, [vorkath, kq], [lance_with_defender])
        
if __name__ == '__main__':
    unittest.main()