DEFAULT_LEVEL_VALUE = 1
DEFAULT_STAT_VALUE = 0
DEFAULT_ATTACK_SPEED = 4

class Monster():
    def __init__(self, data) -> None:
        for key, value in data.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        return self.name == other

    def getSkillLevel(self, skill) -> int:
        return DEFAULT_LEVEL_VALUE if not hasattr(self, "skills") or skill.lower() not in self.skills.keys() else self.skills[skill.lower()]

    def getBonus(self, stat) -> int:
        return DEFAULT_STAT_VALUE if not hasattr(self, "bonuses") or stat.lower() not in self.bonuses.keys() else self.bonuses[stat.lower()]

    def getAttackStyles(self) -> list:
        return self.attack_styles if hasattr(self, "attack_styles") else []

    def getAttackSpeed(self) -> int:
        return self.attack_speed if hasattr(self, "attack_speed") else []

    def getAttributes(self) -> list:
        return self.attributes if hasattr(self, "attributes") else []