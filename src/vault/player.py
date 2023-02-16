from .constants import PLAYER_STATS
class Player():
    def __init__(self, data) -> None:
        for key, value in data.items():
            setattr(self, key, value)
            
    def __str__(self) -> str:
        return '\n'.join([f' - {stat}: {"Empty" if not self.stats[stat] else str(self.stats[stat])}' for stat in PLAYER_STATS])
            
    def getStat(self, stat) -> int:
        return self.stats[stat]