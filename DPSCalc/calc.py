from player import Player
from enemy import NPC
from item import ItemSet
import numpy as np

class DPS():
    def __init__(self, player: Player, enemies: list[NPC], gearsets: list[ItemSet]):
        self.player = player
        self.enemies = enemies
        self.gearsets = gearsets
        
        #Each row is for an individual item set against all enemies
        #TODO configure to read attack style to generate starting thing for mage, range or attack depending
        self.attackRolls = None
        self.defenceRolls = [] 
        
        self.calculateAttackRolls()
        
    def calculateAttackRolls(self):
        attackRolls = []
        for set in self.gearsets:
            if set.attackStyle[1] == 'Ranged':
                attackRolls.append([self.player.getRangedLevel() for i in range(len(self.enemies))])
            
            elif set.attackStyle[1] == 'Mage':
                attackRolls.append([self.player.getMageLevel() for i in range(len(self.enemies))])
             
            elif set.attackStyle[1] in ('Stab', 'Slash', 'Crush'):
                attackRolls.append([self.player.getAttackLevel()  for i in range(len(self.enemies))])   
        
        
        self.attackRolls = np.array(attackRolls)
        print(self.attackRolls)
        #Skipping boosts and prayers for now, but leaving a comment here to indicate that
        self.potionBoosts()
        self.prayerBoosts()
        
        #Checking for void accuracy buffs
        self.voidAccuracyCheck()
        
        #Applying effective level booost from attack stance
        self.addStanceAttackBonus()
        
        #Calculate initial rolls, before equipment modifiers
        self.factorInOffensiveGearBonuses()
        
        #tumekens shadow modifier
        self.tumekensShadowModifier()
        
        #mystic smoke staff
        self.mysticSmokeStaffModifier()
        
        #crystalArmor
        self.crystalArmorModifier()
        
        #salve
        self.salveModifier()
        
        #slayer helm
        self.slayerHelmModifier()
        
        #demonbane spells check
        self.demonbaneSpellsModifier()
        
        #dhcb Modifier
        self.dhcbModifier()
        
        #lance Modifier
        self.lanceModifier()
        
        #wildy weapons
        self.wildyWeaponsModifier()
        
        #tbow
        self.tbowModifier()

        #obsidian armor
        self.obbyArmorModifier()
        
        #chins
        self.chinsModifier()
        
        #inquisitor
        self.inquisitorsModifier()
        
        #tome of water
        self.tomeOfWaterModifier()
        
        #keris partisan of breaching
        self.kerisPartisanOfBreachingModifier()
        print(self.attackRolls)
        
        
    def prayerBoosts(self):
        pass
    
    def potionBoosts(self):
        pass
        
    def voidAccuracyCheck(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            if not (set.body == 'Void knight body' and set.legs == 'Void knight robes' and set.gloves == 'Void knight gloves'):
                continue
            if set.helm == 'Void mage helm' and set.attackStyle[1] == 'Mage':
                self.attackRolls[currSetIndex, :]*=1.45
            elif set.helm == 'Void melee helm' and set.attackStyle[1] in ('Stab', 'Slash', 'Crush'):
                self.attackRolls[currSetIndex, :]*=1.1
            elif set.helm == 'Void ranger helm' and set.attackStyle[1] == 'Ranged':
                self.attackRolls[currSetIndex, :]*=1.1
                
        np.floor(self.attackRolls)
                
                
    
    def addStanceAttackBonus(self):
        #TODO
        pass
    
    def factorInOffensiveGearBonuses(self):
        #TODO
        pass
    
    def tumekensShadowModifier(self):
        pass

    def mysticSmokeStaffModifier(self):
        pass
    
    def crystalArmorModifier(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            if not (set.weapon == 'Bow of faerdhinen' or set.weapon == 'Crystal bow'):
                continue
            multiplier = 1
            if set.helm == 'Crystal helm':
                multiplier += 0.05 
            if set.body == 'Crystal body':
                multiplier += 0.15
            if set.legs == 'Crystal legs':
                multiplier += 0.1
            self.attackRolls[currSetIndex, :] *= multiplier  
        np.floor(self.attackRolls)
                    
    
    def salveModifier(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            #Currently assumes all salves are (ei)
            if not set.necklace == 'Salve amulet':
                continue
            for currEnemyIndex in range(len(self.enemies)):
                if 'Undead' in self.enemies[currEnemyIndex].mobTypes:
                    self.attackRolls[currSetIndex, currEnemyIndex] *= 1.2
        np.floor(self.attackRolls)

    def slayerHelmModifier(self):
        pass
    
    def demonbaneSpellsModifier(self):
        pass
    
    def dhcbModifier(self):
        pass
    
    def lanceModifier(self):
        pass
    
    def wildyWeaponsModifier(self):
        pass
    
    def tbowModifier(self):
        pass
    
    def obbyArmorModifier(self):
        pass
    
    def chinsModifier(self):
        pass
    
    def inquisitorsModifier(self):
        pass
    
    def tomeOfWaterModifier(self):
        pass
    
    def kerisPartisanOfBreachingModifier(self):
        pass