import enum
import html
import requests

SKILLS = enum.Enum(
    "OSRS_LEADERBOARD_SKILLS", [
        "Overall",
        "Attack",
        "Defense",
        "Strength",
        "Hitpoints",
        "Prayer",
        "Magic",
        "Cooking",
        "Woodcutting",
        "Fletching",
        "Fishing",
        "Firemaking",
        "Crafting",
        "Smithing",
        "Mining",
        "Agility",
        "Thieving",
        "Slayer",
        "Farming",
        "Runecrafting",
        "Hunter",
        "Construction",
    ]
)

def load_character_data(character):
    url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={character.name}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"[ERROR] Loading OSRS Highscore Data for '{character.name}'")
        return None

    content = response.content.decode("utf8")
    data = content.split('\n')
    for skill in SKILLS:
        skill_values = data.pop(0)
        character.skills[skill.name] = skill_values.split(",")



class Character():
    def __init__(self, name) -> None:
        self.name = name
        self.skills = {}

    def __repr__(self) -> str:
        return f"Character({self.name})"

    def __str__(self) -> str:
        return f"Character<{self.name}>"
    
    def get_level(self, stat):\
        return 0

    def pretty_print(self, options=[]):
        print(f"============[{self.name}]============")
        if "STATS" in options:
            self.print_stats()

    def print_stats(self):
        for skill_name in self.skills.keys():
            print(f"{skill_name}: \t{self.skills[skill_name][1]}")

if __name__ == "__main__":
    character = Character("Bowfa Good")
    load_character_data(character)
    character.pretty_print(["STATS"])
    #response = load_character_data(Character("MeJrsh"))
    #print(response.content)