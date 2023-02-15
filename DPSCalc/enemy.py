

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
        self.attackBonus = npc[12]
        self.attackStrength = npc[13]
        self.magicAttack = npc[14]
        self.magicStrength = npc[15]
        self.rangedATtack = npc[16]
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