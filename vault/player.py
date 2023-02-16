from constants import PLAYER_STATS
class Player():
    def __init__(self):
        self.stats = {}
        for stat in PLAYER_STATS:
            self.stats[stat] = 99
            
            
    def __str__(self) -> str:
        return '\n'.join([f' - {stat}: {"Empty" if not self.stats[stat] else str(self.stats[stat])}' for stat in PLAYER_STATS])
    
    def setStats(self, stats: dict) -> None:
        for key, value in stats.items():
            self.stats[key] = value
            
    def getStat(self, stat) -> int:
        return self.stats[stat]