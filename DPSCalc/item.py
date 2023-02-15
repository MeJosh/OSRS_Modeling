
class Item():
    def __init__(self, item):
        #I'll likely change this later to have 1 variable / stat, but i cba right now
        #that's a lot of variables to define so im going to be lazy right now
        self.name = item[0]
        self.attackStats = item[1:6]
        self.defenceStats = item[6:11]
        self.strengthStats = item[11:14]
        self.prayerBonus = item[14]
        self.specialInfo = item[15:19]
        self.attackInfo = item[19:22]
        self.miningInfo = item[22]

    def getSlashAccuracy(self):
        return self.attackStats[1]

    def getStabAccuracy(self):
        return self.attackStats[0]

    def getCrushAccuracy(self):
        return self.attackStats[2]

    def getMagicAccuracy(self):
        return self.attackStats[3]

    def getRangeAccuracy(self):
        return self.attackStats[4]

    def getMeleeStrength(self):
        return self.strengthStats[0]

    def getMagicStrength(self):
        return self.strengthStats[2]

    def getRangeStrength(self):
        return self.strengthStats[1]

    def getAttackSpeed(self):
        return self.attackInfo[1]

    def getMageMaxHit(self):
        return self.attackInfo[0]
    
    def getCombatOptions(self):
        return self.attackInfo[2]
    
    def __eq__(self, other):
        return self.name == other
    
    def __str__(self):
        return self.name
    


    

class ItemSet():
    def __init__(self, body: Item, legs: Item, ring: Item, necklace: Item, boots: Item, ammo: Item, helm: Item, weapon: Item, offhand: Item, gloves: Item, cape: Item, attackStyle: list[str]):
        self.body = body
        self.legs = legs
        self.ring = ring
        self.necklace = necklace
        self.boots = boots
        #ammo is also spell used
        #and has corresponding item stats
        self.ammo = ammo
        self.weapon = weapon
        self.offhand = offhand
        self.helm = helm
        self.gloves = gloves
        self.cape = cape
        self.attackStyle = attackStyle
        self.gear = [body, legs, ring, necklace, boots, ammo, helm, weapon, offhand, gloves, cape]


    def __str__(self):
        output = f'Helmet: {self.helm}\n' \
                 f'Ammo: {self.ammo}\n' \
                 f'Necklace: {self.necklace}\n' \
                 f'Cape: {self.cape}\n' \
                 f'Body: {self.body}\n' \
                 f'Weapon: {self.weapon}\n' \
                 f'OffHand: {self.offhand}\n' \
                 f'Legs: {self.legs}\n' \
                 f'Gloves: {self.gloves}\n' \
                 f'Boots: {self.boots}\n' \
                 f'Ring: {self.ring}\n'
        return output
                      

    def getMageAccuracy(self):
        accuracy = 0
        for i in self.gear:
            accuracy += i.getMagicAccuracy()

        return accuracy
    
    def getRangeAccuracy(self):
        accuracy = 0
        for i in self.gear:
            accuracy += i.getRangeAccuracy()
        return accuracy

    def getStabAccuracy(self):
        accuracy = 0
        for i in self.gear:
            accuracy += i.getStabAccuracy()
        return accuracy

    def getSlashAccuracy(self):
        accuracy = 0
        for i in self.gear:
            accuracy += i.getSlashAccuracy()
        return accuracy

    def getCrushAccuracy(self):
        accuracy = 0
        for i in self.gear:
            accuracy += i.getCrushAccuracy()
        return accuracy

    def getMeleeStrength(self):
        strength = 0
        for i in self.gear:
            strength += i.getMeleeStrength()

        return strength

    def getRangeStrength(self):
        strength = 0
        for i in self.gear:
            strength += i.getRangeStrength()

        return strength

    def getMagicStrength(self):
        strength = 0
        for i in self.gear:
            strength += i.getMagicStrength()

        return strength

    def getAttackSpeed(self):
        return self.weapon.getAttackSpeed()