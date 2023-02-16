from player import Player
from enemy import NPC
from item import ItemSet
from constants import MELEE_ATTACK_STANCE_MODIFIER
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
        
        #Checking for void mage accuracy buffs
        self.voidMageAccuracyCheck()
        print(self.attackRolls)
        
        #Applying effective level booost from attack stance
        self.addStanceAttackBonus()
        print(self.attackRolls)
        
        self.otherVoidAccuracyCheck()
        print(self.attackRolls)
        
        #Calculate initial rolls, before equipment modifiers
        self.factorInOffensiveGearBonuses()
        print(self.attackRolls)
        
        #tumekens shadow modifier
        self.tumekensShadowModifier()
        
        #mystic smoke staff
        self.mysticSmokeStaffModifier()
        
        #crystalArmor
        self.crystalArmorModifier()
        print(self.attackRolls)
        
        #salve
        self.salveModifier()
        print(2, self.attackRolls)
        
        #slayer helm
        self.slayerHelmModifier()
        
        #demonbane spells check
        self.demonbaneSpellsModifier()
        
        #dhcb Modifier
        self.dhcbModifier()
        print(1, self.attackRolls)
        
        #lance Modifier
        self.lanceModifier()
        print(self.attackRolls)
        
        #wildy weapons
        self.wildyWeaponsModifier()
        
        #tbow
        self.tbowModifier()
        print(self.attackRolls)

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
        
    def voidMageAccuracyCheck(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            if not (set.body == 'Void knight body' and set.legs == 'Void knight robes' and set.gloves == 'Void knight gloves'):
                continue
            if set.helm == 'Void mage helm' and set.attackStyle[1] == 'Mage':
                self.attackRolls[currSetIndex, :]*=1.45
                
        self.attackRolls = np.floor(self.attackRolls)
                
    def otherVoidAccuracyCheck(self):
        
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            if not (set.body == 'Void knight body' and set.legs == 'Void knight robes' and set.gloves == 'Void knight gloves'):
                continue
            if set.helm == 'Void melee helm' and set.attackStyle[1] in ('Stab', 'Slash', 'Crush'):
                self.attackRolls[currSetIndex, :]*=1.1
            elif set.helm == 'Void ranger helm' and set.attackStyle[1] == 'Ranged':
                self.attackRolls[currSetIndex, :]*=1.1
                
        self.attackRolls = np.floor(self.attackRolls)
                 
    def addStanceAttackBonus(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            attackStyle = set.attackStyle
            if attackStyle[1] in ('Stab', 'Slash', 'Crush'):
                self.attackRolls[currSetIndex, :] += MELEE_ATTACK_STANCE_MODIFIER['Attack'][attackStyle[0]]
            elif attackStyle[1] == 'Ranged':
                self.attackRolls[currSetIndex, :] += MELEE_ATTACK_STANCE_MODIFIER['Ranged'][attackStyle[0]]
            elif attackStyle[1] == 'Mage':
                self.attackRolls[currSetIndex, :] += MELEE_ATTACK_STANCE_MODIFIER['Mage'][attackStyle[0]]
    
    def factorInOffensiveGearBonuses(self):
        for currSetIndex in range(len(self.gearsets)):
            for currEnemyIndex in range(len(self.enemies)):
                self.attackRolls[currSetIndex, currEnemyIndex] *= (64+self.gearsets[currSetIndex].getAccuracyForCurrentStyle())
        
    
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
            print (multiplier)
            self.attackRolls[currSetIndex, :] *= multiplier  
        self.attackRolls = np.floor(self.attackRolls)
                        
    def salveModifier(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            #Currently assumes all salves are (ei)
            if not set.necklace == 'Salve amulet':
                continue
            for currEnemyIndex in range(len(self.enemies)):
                if 'Undead' in self.enemies[currEnemyIndex].mobTypes:
                    self.attackRolls[currSetIndex, currEnemyIndex] *= 1.2
        self.attackRolls = np.floor(self.attackRolls)

    def slayerHelmModifier(self):
        pass
    
    def demonbaneSpellsModifier(self):
        pass
    
    def dhcbModifier(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            if not (set.weapon == 'Dragon hunter crossbow' and set.attackStyle[1] == 'Ranged'):
                continue
            for currEnemyIndex in range(len(self.enemies)):
                if 'Dragon' in self.enemies[currEnemyIndex].mobTypes:
                    self.attackRolls[currSetIndex, currEnemyIndex] *= 1.3
        self.attackRolls = np.floor(self.attackRolls)
    
    def lanceModifier(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            if not (set.weapon == 'Dragon hunter lance' and set.attackStyle[1] in ('Stab', 'Slash', 'Crush')):
                continue
            for currEnemyIndex in range(len(self.enemies)):
                if 'Dragon' in self.enemies[currEnemyIndex].mobTypes:
                    self.attackRolls[currSetIndex, currEnemyIndex] *= 1.2
        self.attackRolls = np.floor(self.attackRolls)
    
    def wildyWeaponsModifier(self):
        pass
    
    #TODO: Update to increase accuracy cap in COX
    def tbowModifier(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            #Currently assumes all tbow usage is outside cox
            if not (set.weapon == 'Twisted bow' or set.attackStyle[1] == 'Ranged'):
                continue
            for currEnemyIndex in range(len(self.enemies)):
                magicCoeff = 3 * max(self.enemies[currEnemyIndex].getMagic(), self.enemies[currEnemyIndex].getMagicBonus())
                if magicCoeff > 750:
                    magicCoeff = 750
                scalar = 140 + int((magicCoeff-10)/100) - int((((magicCoeff/10)-100)**2)/100)
                self.attackRolls[currSetIndex, currEnemyIndex] *= (scalar/100.0)
        
        self.attackRolls = np.floor(self.attackRolls)
                
    
    def obbyArmorModifier(self):
        pass
    
    def chinsModifier(self):
        pass
    
    def inquisitorsModifier(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            if not set.attackStyle[1] == 'Crush':
                continue
            multiplier = 1
            if set.helm == 'Inquisitor\'s great helm':
                multiplier += 0.005
            if set.helm == 'Inquisitor\'s hauberk':
                multiplier += 0.005
            if set.helm == 'Inquisitor\'s plateskirt':
                multiplier += 0.005
                
            if multiplier == 1.015:
                multiplier = 1.025
                
            self.attackRolls[currSetIndex, :]*= multiplier
            
    def tomeOfWaterModifier(self):
        pass
    
    def kerisPartisanOfBreachingModifier(self):
        for currSetIndex in range(len(self.gearsets)):
            set = self.gearsets[currSetIndex]
            if not (set.weapon == 'Keris partisan of breaching'):
                continue
            for currEnemyIndex in range(len(self.enemies)):
                if 'Kalphite' in self.enemies[currEnemyIndex].mobTypes:
                    self.attackRolls[currSetIndex, currEnemyIndex] *= 1.33
        self.attackRolls = np.floor(self.attackRolls)