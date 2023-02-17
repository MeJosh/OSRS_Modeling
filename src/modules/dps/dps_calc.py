import numpy as np
from ...vault.player import Player
from ...vault.monster import Monster
from ...vault.gearset import GearSet
from ...vault.constants import GEAR_STATS, GEAR_SLOTS, ATTACK_STYLE_TYPE_TO_ACCURACY_SKILL, ATTACK_TYPE_TO_BONUS_MAP, ATTACK_STYLE_TYPE_TO_STRENGTH_SKILL, ATTACK_STYLE_TO_GEAR_STRENGTH, ATTACK_STYLE_TYPE_TO_MONSTER_DEFENCE_TYPE

ATTACK_STANCE_MODIFIER = {
    'attack': {
        'controlled': 9,
        'accurate': 11,
        'defensive': 8,
        'aggressive': 8
    },
    'strength': {
        'controlled': 9,
        'accurate': 8,
        'defensive': 8,
        'aggressive': 11
    },
    'defense': {
        'controlled': 9,
        'accurate': 8,
        'defensive': 11,
        'aggressive': 8,
        'longrange': 11
    },
    'magic': {
        'accurate': 11,
        'longrange': 9,
        'defensive': 9
    },
    'ranged' :{
        'rapid': 8,
        'accurate': 11,
        'longrange': 8
    }
}

STANDARD_SPELLS = ['Fire wave']
class DamageCalculator():
    def __init__(self, player: Player, enemies: list[Monster], gearsets: list[GearSet]):
        self.player = player
        self.enemies = enemies
        self.gearsets = gearsets
        
        #Each row is for an individual item set against all enemies
        self.attackRolls = None
        self.maxHits = None
        self.defenseRolls = None 
        
        self.weaponAccuracyRollModifiers = {
            'Crystal bow': self.crystalArmorModifier,
            'Bow of faerdhinen': self.crystalArmorModifier,
            'Dragon hunter lance': self.lanceModifier,
            'Dragon hunter crossbow': self.dhcbModifier,
            'Keris partisan of breaching': self.kerisPartisanOfBreachingModifier,
            'Twisted bow': self.tbowModifier,
            'Mystic smoke staff': self.mysticSmokeStaffModifier,
            'Smoke battlestaff': self.mysticSmokeStaffModifier,
            'Tumeken\'s shadow': self.tumekensShadowModifier,
            'Viggora\'s chainmace': self.wildyWeaponsModifier,
            'Craw\'s bow': self.wildyWeaponsModifier,
            'Thammaron\'s scepter': self.wildyWeaponsModifier,
            'Accrused sceptre': self.wildyWeaponsModifier,
            'Ursine chainmace': self.wildyWeaponsModifier,
            'Webweaver bow': self.wildyWeaponsModifier,
            'Arclight': self.arclightModifier,
            'Gadderhammer': self.gadderHammerModifier,
            'Leaf bladed battleaxe': self.leafBladedBattleaxeModifier
        }
        self.helperFunctionPreGearBonus = [self.potionBoosts, self.prayerBoosts, self.voidMageCheck, self.addStanceBonus, self.otherVoidCheck, self.factorInOffensiveGearBonuses]
        self.helperFunctionPostGearBonus = [self.salveModifier, self.slayerHelmModifier, self.demonbaneSpellsModifier, self.obbyArmorModifier, self.chinsModifier, self.inquisitorsModifier ,self.tomeOfWaterModifier, self.dharoksModifier, self.vampyreWeaponryCheck]
    
        self.CalculateDPSConstants()
        
        
    def CalculateDPSConstants(self):
        attackRolls = []
        maxHits = []
        defRolls = []
        for set in self.gearsets:
            attackRolls.append([self.player.getStat(ATTACK_STYLE_TYPE_TO_ACCURACY_SKILL[set.getStyleType()])  for i in range(len(self.enemies))])
            maxHits.append([self.player.getStat(ATTACK_STYLE_TYPE_TO_STRENGTH_SKILL[set.getStyleType()]) for i in range(len(self.enemies))])
            temp = []
            for enemy in self.enemies:
                temp.append((9+enemy.getSkillLevel('defense'))*(64+enemy.getBonus(ATTACK_STYLE_TYPE_TO_MONSTER_DEFENCE_TYPE[set.getStyleType()])))
            defRolls.append(temp)   
        
        self.attackRolls = np.array(attackRolls)
        self.maxHits = np.array(maxHits)
        self.defenseRolls = np.array(defRolls)
        
        for i in range(len(self.attackRolls)):
            
            for helperFunc in self.helperFunctionPreGearBonus:
                helperFunc(i)
            
            if (self.gearsets[i].getItemInSlot(GEAR_SLOTS.WEAPON).name in self.weaponAccuracyRollModifiers):
                self.weaponAccuracyRollModifiers[self.gearsets[i].getItemInSlot(GEAR_SLOTS.WEAPON)](i)
            
            for helperFunc in self.helperFunctionPostGearBonus:
                helperFunc(i)
        
          
    def prayerBoosts(self, setIndex):
        pass
    
    def potionBoosts(self, setIndex):
        pass
    
    def brimstoneRingModifier(self, setIndex):
        if not set.getItemInSlot(GEAR_SLOTS.RING) == 'Brimstone ring':
            return
        self.defenseRolls *= 0.975
        self.defenseRolls = np.floor(self.defenseRolls)
        
    def voidMageCheck(self, setIndex):
        set = self.gearsets[setIndex]
        if not (set.getItemInSlot(GEAR_SLOTS.BODY) == 'Void knight body' and set.getItemInSlot(GEAR_SLOTS.LEGS) == 'Void knight robes' and set.getItemInSlot(GEAR_SLOTS.HANDS) == 'Void knight gloves'):
            return
        if set.getItemInSlot(GEAR_SLOTS.HEAD) == 'Void mage helm' and set.getStyleType() == 'Mage':
            self.attackRolls[setIndex, :]*=1.45    
            self.attackRolls = np.floor(self.attackRolls)
                
    #Currently assumes all void is regular void
    def otherVoidCheck(self, setIndex):   
        set = self.gearsets[setIndex]
        if not (set.getItemInSlot(GEAR_SLOTS.BODY) == 'Void knight body' and set.getItemInSlot(GEAR_SLOTS.LEGS) == 'Void knight robes' and set.getItemInSlot(GEAR_SLOTS.HANDS) == 'Void knight gloves'):
            return
        if set.getItemInSlot(GEAR_SLOTS.HEAD) == 'Void melee helm' and set.getStyleType() in ('Stab', 'Slash', 'Crush'):
            self.attackRolls[setIndex, :]*=1.1
            self.maxHits *= 1.1
            self.maxHits = np.floor(self.maxHits)
            self.attackRolls = np.floor(self.attackRolls)
        elif set.getItemInSlot(GEAR_SLOTS.HEAD) == 'Void ranger helm' and set.getStyleType() == 'Ranged':
            self.attackRolls[setIndex, :]*=1.1
            self.maxHits *= 1.1
            self.maxHits = np.floor(self.maxHits)
            self.attackRolls = np.floor(self.attackRolls)
                 
    def addStanceBonus(self, setIndex):
        styleType = self.gearsets[setIndex].getStyleType()
        weaponStyle = self.gearsets[setIndex].getWeaponStyle()
        self.attackRolls[setIndex, :] += ATTACK_STANCE_MODIFIER[ATTACK_STYLE_TYPE_TO_ACCURACY_SKILL[styleType].lower()][weaponStyle.lower()]
        self.maxHits[setIndex, :] += ATTACK_STANCE_MODIFIER[ATTACK_STYLE_TYPE_TO_STRENGTH_SKILL[styleType].lower()][weaponStyle.lower()]
    
    def factorInOffensiveGearBonuses(self, setIndex):
        self.attackRolls[setIndex, :] *= (64+self.gearsets[setIndex].getBonus(ATTACK_TYPE_TO_BONUS_MAP[self.gearsets[setIndex].getStyleType()]))
        styleType = self.gearsets[setIndex].getStyleType().upper()
        self.maxHits[setIndex,:] =0.5 + self.maxHits[setIndex,:]*(64+self.gearsets[setIndex].getBonus(ATTACK_STYLE_TO_GEAR_STRENGTH[styleType])) / 640
        self.maxHits = np.floor(self.maxHits)
         
    #TODO Only considers enemies to be outside of TOA
    def tumekensShadowModifier(self, setIndex):
        self.attackRolls[setIndex, :] *= 3

    def mysticSmokeStaffModifier(self, setIndex):
        if not self.gearsets[setIndex].getItemInSlot(GEAR_SLOTS.AMMUNITION).name in STANDARD_SPELLS:
            return
        self.attackRolls[setIndex] *= 1.1
        self.attackRolls = np.floor(self.attackRolls)
    
    def crystalArmorModifier(self, setIndex):
        set = self.gearsets[setIndex]
        multiplier = 1
        if set.getItemInSlot(GEAR_SLOTS.HEAD) == 'Crystal helm':
            multiplier += 0.05 
        if set.getItemInSlot(GEAR_SLOTS.BODY) == 'Crystal body':
            multiplier += 0.15
        if set.getItemInSlot(GEAR_SLOTS.LEGS) == 'Crystal legs':
            multiplier += 0.1
        self.attackRolls[setIndex, :] *= multiplier
        self.maxHits[setIndex, :] *= multiplier
        self.maxHits = np.floor(self.maxHits)
        self.attackRolls = np.floor(self.attackRolls)
                        
    def salveModifier(self, setIndex):
        set = self.gearsets[setIndex]
        #Currently assumes all salves are (ei)
        if not set.getItemInSlot(GEAR_SLOTS.NECK) == 'Salve amulet':
            return
        for currEnemyIndex in range(len(self.enemies)):
            if 'Undead' in self.enemies[currEnemyIndex].attributes:
                self.attackRolls[setIndex, currEnemyIndex] *= 1.2
                self.maxHits[setIndex, :] *= 1.2
        self.maxHits = np.floor(self.maxHits)
        self.attackRolls = np.floor(self.attackRolls)

    def slayerHelmModifier(self, setIndex):
        pass
    
    def demonbaneSpellsModifier(self, setIndex):
        pass
    
    def dhcbModifier(self, setIndex):
        for currEnemyIndex in range(len(self.enemies)):
            if 'Draconic' in self.enemies[currEnemyIndex].attributes:
                self.attackRolls[setIndex, currEnemyIndex] *= 1.3                
                self.maxHits[setIndex, :] *= 1.25
        self.maxHits = np.floor(self.maxHits)
        self.attackRolls = np.floor(self.attackRolls)
    
    def lanceModifier(self, setIndex):
        for currEnemyIndex in range(len(self.enemies)):
            if 'Draconic' in self.enemies[currEnemyIndex].attributes:
                self.attackRolls[setIndex, currEnemyIndex] *= 1.2
                self.maxHits[setIndex, :] *= 1.2
        self.maxHits = np.floor(self.maxHits)
        self.attackRolls = np.floor(self.attackRolls)
    
    def wildyWeaponsModifier(self, setIndex):
        pass
    
    #TODO: Update to increase accuracy cap in COX
    def tbowModifier(self, setIndex):
        #Currently assumes all tbow usage is outside cox
        for currEnemyIndex in range(len(self.enemies)):
            magicCoeff = 3 * max(self.enemies[currEnemyIndex].getMagic(), self.enemies[currEnemyIndex].getMagicBonus())
            if magicCoeff > 750:
                magicCoeff = 750
            scalar = 140 + int((magicCoeff-10)/100) - int((((magicCoeff/10)-100)**2)/100)
            self.attackRolls[setIndex, currEnemyIndex] *= (scalar/100.0)
        
        self.attackRolls = np.floor(self.attackRolls)
                
    def obbyArmorModifier(self, setIndex):
        pass
    
    def chinsModifier(self, setIndex):
        pass
    
    def inquisitorsModifier(self, setIndex):
        set = self.gearsets[setIndex]
        if not set.getStyleType() == 'Crush':
            return
        multiplier = 0
        if set.getItemInSlot(GEAR_SLOTS.HEAD) == 'Inquisitor\'s great helm':
            multiplier += 1
        if set.getItemInSlot(GEAR_SLOTS.BODY) == 'Inquisitor\'s hauberk':
            multiplier += 1
        if set.getItemInSlot(GEAR_SLOTS.LEGS) == 'Inquisitor\'s plateskirt':
            multiplier += 1
            
        if multiplier == 3:
            multiplier = 5
            
        self.attackRolls[setIndex, :]*= 1+ (0.005*multiplier)
        self.maxHits[setIndex, :] *= 1 + (0.005*multiplier)
        self.maxHits = np.floor(self.maxHits)
        self.attackRolls = np.floor(self.attackRolls)
            
    def tomeOfWaterModifier(self, setIndex):
        if not self.gearsets[setIndex].getItemInSlot(GEAR_SLOTS.SHIELD) == 'Tome of water' \
            or not self.gearsets[setIndex].getItemInSlot(GEAR_SLOTS.AMMUNITION).name in ('Water Strike', 'Water bolt', 'Water blast', 'Water wave', 'Water surge')\
            or not self.gearsets[setIndex].getItemInSlot(GEAR_SLOTS.WEAPON).getStyleType() == 'Magic':
            return
        
        self.attackRolls[setIndex, :] *= 1.2
    
    def kerisPartisanOfBreachingModifier(self, setIndex):
        for currEnemyIndex in range(len(self.enemies)):
            if 'Kalphite' in self.enemies[currEnemyIndex].attributes:
                self.attackRolls[setIndex, currEnemyIndex] *= 1.33
                self.maxHits[setIndex, :] *= 1.33
        self.maxHits = np.floor(self.maxHits)
        self.attackRolls = np.floor(self.attackRolls)
        
    def arclightModifier(self, setIndex):
        for currEnemyIndex in range(len(self.enemies)):
            if 'Demon' in self.enemies[currEnemyIndex].attributes:
                self.attackRolls[setIndex, currEnemyIndex] *= 1.7
                self.maxHits[setIndex, :] *= 1.7
        self.maxHits = np.floor(self.maxHits)
        self.attackRolls = np.floor(self.attackRolls)
        

    def vampyreWeaponryCheck(self, setIndex):
        pass
    
    #Need to sort out boost structure first, as currentHp will reside in that object
    def dharoksModifier(self, setIndex):
        pass
    
    def leafBladedBattleaxeModifier(self, setIndex):
        for idx, enemy in enumerate(self.enemies):
            if enemy == 'Kurask' or enemy == 'Turoth':
                self.maxHits[setIndex, idx] *= 1.175
        self.maxHits = np.floor(self.maxHits)
        
    def gadderHammerModifier(self, setIndex):
        for idx, enemy in enumerate(self.enemies):
            if 'Shade' in enemy.attributes:
                self.maxHits[setIndex, idx] *= 1.25
        self.maxHits = np.floor(self.maxHits)
                
