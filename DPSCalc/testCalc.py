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

class TestItemSet(unittest.TestCase):
    def test_summingRangedAccuracy(self):
        self.assertEquals(crystal_with_bowfa.getRangedAccuracy(), 186, 'Item set ranged accuracy should be 186')
        
    def test_summingRangedStrength(self):
        self.assertEquals(crystal_with_bowfa.getRangeStrength(), 106, 'Item set ranged accuracy should be 106')
        
class TestDPSCalculation(unittest.TestCase):
    def test_attackRollCalculationWithTbowAndCrystal(self):
        dpsObject = DPS(maxedPlayer, [vorkath], [crystal_with_tbow, crystal_with_bowfa])
        dpsObject.attackRolls = np.array([[100.0], [100.0]])
        dpsObject.crystalArmorModifier()
        self.assertEquals(dpsObject.attackRolls[0][0], 100, 'Crystal armor boosting non-crystal weaponry')
        self.assertEquals(dpsObject.attackRolls[1][0], 130, 'Crystal armor not boosting crystal weaponry')
        
    def testVoidRangeAccuracyWhenValid(self):
        dpsObject = DPS(maxedPlayer, [vorkath], [void_with_bowfa])
        dpsObject.attackRolls = np.array([[100.0]])
        dpsObject.otherVoidAccuracyCheck()
        self.assertEquals(dpsObject.attackRolls[0][0], 110, 'Void not boosting accuracy when ranging')
        
    def testVoidRangeAccuracyWhenUsingMelee(self):
        dpsObject = DPS(maxedPlayer, [vorkath], [ranged_void_with_lance, melee_void_with_lance])
        dpsObject.attackRolls = np.array([[100.0], [100.0]])
        dpsObject.otherVoidAccuracyCheck()
        self.assertEquals(dpsObject.attackRolls[0][0], 100, 'Void range is boosting melee weapons')
        self.assertEquals(dpsObject.attackRolls[1][0], 110, 'Void melee isn\'t boosting accuracy')
        
    def test_SalveAmuletBoostWhenWearingSalve(self):
        dpsObject = DPS(maxedPlayer, [vorkath], [dhcb_with_salve, crystal_with_bowfa])
        dpsObject.attackRolls = np.array([[100.0], [100.0]])
        dpsObject.salveModifier()
        self.assertEquals(dpsObject.attackRolls[0][0], 120, 'Salve isn\'t boosting correctly')
        self.assertEquals(dpsObject.attackRolls[1][0], 100, 'Salve is boosting accuracy when not equipped')
        
    def test_DHCB(self):
        dpsObject = DPS(maxedPlayer, [vorkath], [dhcb_with_salve])
        dpsObject.attackRolls = np.array([[100.0]])
        dpsObject.dhcbModifier()
        self.assertEquals(dpsObject.attackRolls[0][0], 130, 'DHCB not applying bonus accuracy')
        
    def test_DHL(self):
        dpsObject = DPS(maxedPlayer, [vorkath], [lance_with_defender])
        dpsObject.attackRolls = np.array([[100.0]])
        dpsObject.lanceModifier()
        self.assertEquals(dpsObject.attackRolls[0][0], 120, 'DHL not applying bonus accuracy')
            
    def test_VoidMage(self):
        dpsObject = DPS(maxedPlayer, [vorkath], [void_mage, void_mage_with_melee])
        dpsObject.attackRolls = np.array([[100.0], [100.0]])
        dpsObject.voidMageAccuracyCheck()
        self.assertEquals(dpsObject.attackRolls[0][0], 145, 'Void mage ins\'t boosting correctly')
        self.assertEquals(dpsObject.attackRolls[1][0], 100, 'Void mage is boosting non-mage based attacks')\
            
    def test_Inquisitors(self):
        dpsObject = DPS(maxedPlayer, [vorkath], [inquis_crush, inquis_notCrush, partialInquis_crush])
        dpsObject.attackRolls = np.array([[1000.0], [1000.0], [1000.0]])
        dpsObject.inquisitorsModifier()
        self.assertAlmostEqual(dpsObject.attackRolls[0][0], 1025, msg='Inquis not boosting correctly', delta=0.01)
        self.assertEquals(dpsObject.attackRolls[1][0], 1000, 'Inquis boosting non crush weaponry')
        self.assertEquals(dpsObject.attackRolls[2][0], 1010, 'Inquis not boosting correct amount for partial set')
        
    def test_KerisPartisanOfBreaching(self):
        dpsObject = DPS(maxedPlayer, [kq, vorkath], [partialInquis_crush, inquis_crush])
        dpsObject.attackRolls = np.array([[100.0, 100.0], [100.0, 100.0]])
        dpsObject.kerisPartisanOfBreachingModifier()
        self.assertEquals(dpsObject.attackRolls[0][0], 133, 'Partisan not proccing on kalphite')
        self.assertEquals(dpsObject.attackRolls[0][1], 100, 'Partisan proccing on non kalphite')
        self.assertEquals(dpsObject.attackRolls[1][0], 100, 'Partisan effect proccing against kalphite while not wielding keris')
        self.assertEquals(dpsObject.attackRolls[1][1], 100, 'Partisan proccing for no good reason')
        
if __name__ == '__main__':
    unittest.main()