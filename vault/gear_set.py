from constants import GEAR_SLOTS, ATTACK_TYPES, ATTACK_STYLES, ATTACK_TYPE_TO_BONUS_MAP

class GearSet():
    def __init__(self):
        self.items = {}
        for slot in GEAR_SLOTS:
            self.items[slot] = None

        # Set default values for Unarmed - Punch
        self.attack_type = ATTACK_TYPES.CRUSH.lower()
        self.attack_style = ATTACK_STYLES.ACCURATE.lower()

    def __str__(self) -> str:
        return '\n'.join([f' - {slot}: {"Empty" if not self.items[slot] else str(self.items[slot])}' for slot in GEAR_SLOTS])

    def setItemInSlot(self, slot, item) -> bool:
        # TODO: This should check that the slot is a correct match, and if not return error
        
        self.items[slot] = item

        # If we are equipping a weapon, check if we need to reset the attack style
        if slot == GEAR_SLOTS.WEAPON:
            valid_styles = item.getAttackStyles()
            
            # TODO: This should be a smarter check as seen below, but brain is too tired right now - so we'll just hard reset
            self.attack_style = next(iter(valid_styles))
            self.attack_type = valid_styles[self.attack_style]["style_type"]

            # First check if the attack style lines up
            # if self.attack_style not in valid_styles.keys():
            #    self.attack_style = next(iter(valid_styles))
            #    self.attack_type = valid_styles[self.attack_style]["style_type"]
        
    def setAttackStyle(self, style) -> bool:
        self.attack_style = style

    def getAttackStyles(self) -> list:
        return list(self.items[GEAR_SLOTS.WEAPON].getAttackStyles().keys()) if self.items[GEAR_SLOTS.WEAPON] is not None \
            else [ATTACK_STYLES.ACCURATE.value.lower(), ATTACK_STYLES.AGGRESSIVE.value.lower(), ATTACK_STYLES.DEFENSIVE.value.lower()]

    def getBonus(self, stat) -> int:
        return sum([0 if not item else item.getBonus(stat) for item in self.items.values()])

    def getAttackSpeed(self) -> int:
        return 4 if self.items[GEAR_SLOTS.WEAPON] is None else self.items[GEAR_SLOTS.WEAPON].attack_speed

    def getAttackBonus(self, attack_stat=None) -> float:
        if not attack_stat:
            attack_stat = ATTACK_TYPE_TO_BONUS_MAP[self.attack_type]
        
        return sum([0 if self.items[slot] is None else self.items[slot].getBonus(attack_stat) for slot in GEAR_SLOTS])


