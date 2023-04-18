from .constants import PLAYER_STATS
class Player():
    def __init__(self, data) -> None:
        for key, value in data.items():
            setattr(self, key, value)
            
    def __str__(self) -> str:
        return '\n'.join([f' - {stat}: {str(self.skills[stat.lower()])}' for stat in PLAYER_STATS])
            
    def getStat(self, stat) -> int:
        return self.skills[stat.lower()]