class Item():
    def __init__(self, data) -> None:
        for key, value in data.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def getBonus(self, stat) -> int:
        stat = stat.lower()
        return 0 if not hasattr(self, "bonuses" or stat not in self.bonuses.keys()) else self.bonuses[stat]

    def getAttackStyles(self) -> dict:
        if not hasattr(self, "attack_styles"):
            return []
        return self.attack_styles
