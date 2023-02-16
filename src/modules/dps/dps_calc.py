from vault.player import Player
from vault.monster import Monster
from vault.gearset import GearSet
from vault.constants import GEAR_STATS, GEAR_SLOTS
import numpy as np

ATTACK_STANCE_MODIFIER = {
    'Attack': {
        'Controlled': 9,
        'Accurate': 11,
        'Defensive': 8,
        'Aggressive': 8
    },
    'Strength': {
        'Controlled': 9,
        'Accurate': 8,
        'Defensive': 8,
        'Aggressive': 11
    },
    'Defence': {
        'Controlled': 9,
        'Accurate': 8,
        'Defensive': 11,
        'Aggressive': 8,
        'Longrange': 11
    },
    'Mage': {
        'Accurate': 11,
        'Longrange': 9,
        'Defensive': 9
    },
    'Ranged' :{
        'Rapid': 8,
        'Accurate': 11,
        'Longrange': 8
    }
}

class DamageCalculator():
    def __init__(self, player: Player, enemies: list[Monster], gearsets: list[GearSet]):
        self.player = player
        self.enemies = enemies
        self.gearsets = gearsets
        
        #Each row is for an individual item set against all enemies
        self.attackRolls = None
        self.defenceRolls = [] 
        
        self.weaponAccuracyRollModifiers = {
            'Crystal bow': self.crystalArmorModifier,
            'Bow of faerdhinen': self.crystalArmorModifier,
            'Dragon hunter lance': self.lanceModifier,
            'Dragon hunter crossbow': self.dhcbModifier,
            'Keris partisan of breaching': self.kerisPartisanOfBreachingModifier,
            'Twisted bow': self.tbowModifier,
            'Mystic smoke staff': self.mysticSmokeStaffModifier,
            'Tumeken\'s shadow': self.tumekensShadowModifier,
            'Viggora\'s chainmace': self.wildyWeaponsModifier,
            'Craw\'s bow': self.wildyWeaponsModifier,
            'Thammaron\'s scepter': self.wildyWeaponsModifier,
            'Accrused sceptre': self.wildyWeaponsModifier,
            'Ursine chainmace': self.wildyWeaponsModifier,
            'Webweaver bow': self.wildyWeaponsModifier
        }
    
        self.calculateMaxAttackRolls()
        
        
    def calculateMaxAttackRolls(self):
        attackRolls = []
        for set in self.gearsets:
            #TODO: Replace instances of 'ranged', 'mage', and ('Stab', 'Slash', 'Crush') with constants everywhere
            if set.attackStyle[1] == 'Ranged':
                attackRolls.append([self.player.getRangedLevel() for i in range(len(self.enemies))])
            
            elif set.attackStyle[1] == 'Mage':
                attackRolls.append([self.player.getMageLevel() for i in range(len(self.enemies))])
             
            elif set.attackStyle[1] in ('Stab', 'Slash', 'Crush'):
                attackRolls.append([self.player.getAttackLevel()  for i in range(len(self.enemies))])   
        
        
        self.attackRolls = np.array(attackRolls)
        
        for i in range(len(self.attackRolls)):
            #Skipping boosts and prayers for now, but leaving a comment here to indicate that
            self.potionBoosts()
            self.prayerBoosts()
            
            #Checking for void mage accuracy buffs
            self.voidMageAccuracyCheck(i)
            print (self.attackRolls)
            
            #Applying effective level booost from attack stance
            self.addStanceAttackBonus(i)
            print (self.attackRolls)
            
            self.otherVoidAccuracyCheck(i)
            print (self.attackRolls)
            
            #Calculate initial rolls, before equipment modifiers
            self.factorInOffensiveGearBonuses(i)
            
            print (self.attackRolls)
            if (self.gearsets[i].weapon.name in self.weaponAccuracyRollModifiers):
                self.weaponAccuracyRollModifiers[self.gearsets[i].weapon.name](i)
            print (self.attackRolls)
            #salve
            self.salveModifier(i)
            
            #slayer helm
            self.slayerHelmModifier()
            
            #demonbane spells check
            self.demonbaneSpellsModifier()
            
            #obsidian armor
            self.obbyArmorModifier()
            
            #chins
            self.chinsModifier()
            
            #inquisitor
            self.inquisitorsModifier(i)
            
            #tome of water
            self.tomeOfWaterModifier()
        print (self.attackRolls)
        
          
    def prayerBoosts(self):
        pass
    
    def potionBoosts(self):
        pass
        
    def voidMageAccuracyCheck(self, setIndex):
        set = self.gearsets[setIndex]
        if not (set.body == 'Void knight body' and set.legs == 'Void knight robes' and set.gloves == 'Void knight gloves'):
            return
        if set.helm == 'Void mage helm' and set.attackStyle[1] == 'Mage':
            self.attackRolls[setIndex, :]*=1.45    
            self.attackRolls = np.floor(self.attackRolls)
                
    def otherVoidAccuracyCheck(self, setIndex):   
        set = self.gearsets[setIndex]
        if not (set.body == 'Void knight body' and set.legs == 'Void knight robes' and set.gloves == 'Void knight gloves'):
            return
        if set.helm == 'Void melee helm' and set.attackStyle[1] in ('Stab', 'Slash', 'Crush'):
            self.attackRolls[setIndex, :]*=1.1
            self.attackRolls = np.floor(self.attackRolls)
        elif set.helm == 'Void ranger helm' and set.attackStyle[1] == 'Ranged':
            self.attackRolls[setIndex, :]*=1.1
            self.attackRolls = np.floor(self.attackRolls)
                 
    def addStanceAttackBonus(self, setIndex):
        attackStyle = self.gearsets[setIndex].attackStyle
        if attackStyle[1] in ('Stab', 'Slash', 'Crush'):
            self.attackRolls[setIndex, :] += ATTACK_STANCE_MODIFIER['Attack'][attackStyle[0]]
        else:
            self.attackRolls[setIndex, :] += ATTACK_STANCE_MODIFIER[attackStyle[1]][attackStyle[0]]
    
    def factorInOffensiveGearBonuses(self, setIndex):
        self.attackRolls[setIndex, :] *= (64+self.gearsets[setIndex].getAccuracyForCurrentStyle())
         
    def tumekensShadowModifier(self, setIndex):
        pass

    def mysticSmokeStaffModifier(self, setIndex):
        pass
    
    def crystalArmorModifier(self, setIndex):
        set = self.gearsets[setIndex]
        multiplier = 1
        if set.helm == 'Crystal helm':
            multiplier += 0.05 
        if set.body == 'Crystal body':
            multiplier += 0.15
        if set.legs == 'Crystal legs':
            multiplier += 0.1
        self.attackRolls[setIndex, :] *= multiplier  
        self.attackRolls = np.floor(self.attackRolls)
                        
    def salveModifier(self, setIndex):
        set = self.gearsets[setIndex]
        #Currently assumes all salves are (ei)
        if not set.necklace == 'Salve amulet':
            return
        for currEnemyIndex in range(len(self.enemies)):
            if 'Undead' in self.enemies[currEnemyIndex].mobTypes:
                self.attackRolls[setIndex, currEnemyIndex] *= 1.2
        self.attackRolls = np.floor(self.attackRolls)

    def slayerHelmModifier(self):
        pass
    
    def demonbaneSpellsModifier(self):
        pass
    
    def dhcbModifier(self, setIndex):
        set = self.gearsets[setIndex]
        for currEnemyIndex in range(len(self.enemies)):
            if 'Dragon' in self.enemies[currEnemyIndex].mobTypes:
                self.attackRolls[setIndex, currEnemyIndex] *= 1.3
        self.attackRolls = np.floor(self.attackRolls)
    
    def lanceModifier(self, setIndex):
        set = self.gearsets[setIndex]
        for currEnemyIndex in range(len(self.enemies)):
            if 'Dragon' in self.enemies[currEnemyIndex].mobTypes:
                self.attackRolls[setIndex, currEnemyIndex] *= 1.2
        self.attackRolls = np.floor(self.attackRolls)
    
    def wildyWeaponsModifier(self, setIndex):
        pass
    
    #TODO: Update to increase accuracy cap in COX
    def tbowModifier(self, setIndex):
        set = self.gearsets[setIndex]
        #Currently assumes all tbow usage is outside cox
        for currEnemyIndex in range(len(self.enemies)):
            magicCoeff = 3 * max(self.enemies[currEnemyIndex].getMagic(), self.enemies[currEnemyIndex].getMagicBonus())
            if magicCoeff > 750:
                magicCoeff = 750
            scalar = 140 + int((magicCoeff-10)/100) - int((((magicCoeff/10)-100)**2)/100)
            self.attackRolls[setIndex, currEnemyIndex] *= (scalar/100.0)
        
        self.attackRolls = np.floor(self.attackRolls)
                
    def obbyArmorModifier(self):
        pass
    
    def chinsModifier(self):
        pass
    
    def inquisitorsModifier(self, setIndex):
        set = self.gearsets[setIndex]
        if not set.attackStyle[1] == 'Crush':
            return
        multiplier = 0
        if set.helm == 'Inquisitor\'s great helm':
            multiplier += 1
        if set.body == 'Inquisitor\'s hauberk':
            multiplier += 1
        if set.legs == 'Inquisitor\'s plateskirt':
            multiplier += 1
            
        if multiplier == 3:
            multiplier = 5
            
        self.attackRolls[setIndex, :]*= 1+ (0.005*multiplier)
        self.attackRolls = np.floor(self.attackRolls)
            
    def tomeOfWaterModifier(self):
        pass
    
    def kerisPartisanOfBreachingModifier(self, setIndex):
        set = self.gearsets[setIndex]
        for currEnemyIndex in range(len(self.enemies)):
            if 'Kalphite' in self.enemies[currEnemyIndex].mobTypes:
                self.attackRolls[setIndex, currEnemyIndex] *= 1.33
        self.attackRolls = np.floor(self.attackRolls)
        
