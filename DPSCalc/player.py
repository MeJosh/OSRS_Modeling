from item import ItemSet

class Player():
    def __init__(self, attack: int, defence: int, strength: int, ranged: int, mage: int, maxHp: int, currHp: int): #, equipment: ItemSet):
        self.attack = attack
        self.defence = defence
        self.strength = strength
        self.ranged = ranged
        self.mage = mage
        self.maxHp = maxHp
        self.currHp = currHp
        #Unsure if this will be attached or passed around.. likely passed around since there will be multiple on the same player
        #self.equipment = equipment

    def getAttackLevel(self):
        return self.attack

    def getStrengthLevel(self):
        return self.strength
    
    def getDefenceLevel(self):
        return self.defence
    
    def getRangedLevel(self):
        return self.ranged
        
    def getMageLevel(self):
        return self.mage

    