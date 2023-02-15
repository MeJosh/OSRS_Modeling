

class NPC():
    def __init__(self, npc):
        self.name = npc[0]
        self.hp = npc[4]
        self.attack = npc[5]
        self.strength = npc[6]
        self.defence = npc[7]
        self.magic = npc[8]
        self.ranged = npc[9]
        self.attackSpeed = npc[11]
        self.attackStyle = npc[10]
        self.meleeBonus = npc[12]
        self.meleeStrength = npc[13]
        self.magicBonus = npc[14]
        self.magicStrength = npc[15]
        self.rangedBonus = npc[16]
        self.rangedStrength = npc[17]
        self.stabDef = npc[18]
        self.slashDef = npc[19]
        self.crushDef = npc[20]
        self.mageDef = npc[21]
        self.rangedDef = npc[22]
        self.mobTypes = npc[24]
        self.defenceFloor = npc[26]
        
    def __str__(self):
        return self.name

    def getName(self):
        return self.name
    
    def getHp(self):
        return self.hp
    
    def getAttack(self):
        return self.attack
    
    def getStrength(self):
        return self.strength
    
    def getDefence(self):
        return self.defence
    
    def getMagic(self):
        return self.magic
    
    def getRanged(self):
        return self.ranged
    
    def getAttackSpeed(self):
        return self.attackSpeed
    
    def getAttackStyle(self):
        return self.attackStyle
    
    def getMeleeBonus(self):
        return self.meleeBonus
    
    def getMeleeStrength(self):
        return self.meleeStrength
    
    def getMagicStrength(self):
        return self.magicStrength
    
    def getMagicBonus(self):
        return self.magicBonus
    
    def getMagicStrength(self):
        return self.magicStrength
    
    def getRangedBonus(self):
        return self.rangedBonus
    
    def getRangedStrength(self):
        return self.rangedStrength
    
    def getStabDefence(self):
        return self.stabDef
    
    def getSlashDefence(self):
        return self.slashDef
    
    def getCrushDefence(self):
        return self.crushDef
    
    def getMageDefence(self):
        return self.mageDef
    
    def getRangedDefence(self):
        return self.rangedDef
    
    def getMobTypes(self):
        return self.mobTypes
    
    def getDefenceFloor(self):
        return self.defenceFloor