import urllib.request
import urllib.parse
import json
import yaml
import os
from datetime import date
from shutil import copyfile
from os.path import exists



BOSSES = [
    "Bounty Hunter - Hunter",
    "Bounty Hunter - Rogue",
    "Clue Scrolls (All)",
    "Clue Scrolls (Beginner)",
    "Clue Scrolls (Easy)",
    "Clue Scrolls (Medium)",
    "Clue Scrolls (Hard)",
    "Clue Scrolls (Elite)",
    "Clue Scrolls (Master)",
    "LMS - Rank",
    "Soul Wars Zeal",
    "Abyssal Sire",
    "Alchemical Hydra",
    "Barrows Chests",
    "Bryophyta",
    "Callisto",
    "Cerberus",
    "Chambers of Xeric",
    "Chambers of Xeric: Challenge Mode",
    "Chaos Elemental",
    "Chaos Fanatic",
    "Commander Zilyana",
    "Corporeal Beast",
    "Crazy Archaeologist",
    "Dagannoth Prime",
    "Dagannoth Rex",
    "Dagannoth Supreme",
    "Deranged Archaeologist",
    "General Draardor",
    "Giant Mole",
    "Grotesque Guardians",
    "Hespori",
    "Kalphite Queen",
    "King Black Dragon",
    "Kraken",
    "Kree'Arra",
    "K'ril Tsutsaroth",
    "Mimic",
    "Nightmare",
    "Phosani's Nightmare",
    "Orbor",
    "Sarachnis",
    "Scorpia",
    "Skotizo",
    "Tempoross",
    "The Gauntlet",
    "The Corrupted Gauntlet",
    "Theatre of Blood",
    "Theatre of Blood: Hard Mode",
    "Thermonuclear Smoke Devil",
    "TzKal-Zuk",
    "TzKal-Jad",
    "Vet'ion",
    "Vorkath",
    "Wintertodt",
    "Zalcano",
    "Zulrah"
]

def loadCharacterData(character):
    url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={character}"
    url = url.format(character = urllib.parse.quote_plus(character))
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
    print(url)
    req = urllib.request.Request(url, headers=hdr)
    with urllib.request.urlopen(req) as response:
        if response.status_code != 200:
            print("Error: " + str(response.status_code))
            return ""
        html = response.read()
        data = formatCharacterData(html.decode('utf8'))
        data["character"] = character
        return data

def formatCharacterData(data):
    result = {}

    data = data.split('\n')
    #print(data)

    result["skills"] = {}
    '''for SKILL in SKILLS:
        skill_data = data.pop(0)
        result["skills"][SKILL] = skill_data.split(",")'''

    result["bosses"] = {}
    for BOSS in BOSSES:
        boss_data = data.pop(0)
        result["bosses"][BOSS] = boss_data.split(",")

    return result

def writeCharacterDataToFile(data, dir):
    character_name = data["character"]
    print(dir)

    '''path = ""
    for segment in dir.split("/"):
        path += segment
        print("Checking: " + path)
        if not exists(path):
            os.mkdir(path=path)'''


    if not exists(dir):
        os.mkdir(path=dir)

    ref_filename = dir + "{character}_latest.json".format(character = character_name)
    if(exists(ref_filename)):
        with open(ref_filename, 'r') as file:
            ref_data = file.readline().strip()
            ref_data.replace("'", "\"")
            ref_data = json.loads(str(ref_data))
            if ref_data["skills"]["Overall"][2] == data["skills"]["Overall"][2]:
                return

    filename = dir + "{character}_{date}.json".format(character = character_name, date = date.today())
    with open(filename, 'w') as file:
        file.write(json.dumps(data))

    copyfile(filename, ref_filename)

def getCharacterListFromConfig(config_path):
    with open(config_path, "r") as file:
        try:
            return yaml.safe_load(file)["characters"]
        except yaml.YAMLError as exc:
            print(exc)
            return []

if __name__ == "__main__":
    character_list = getCharacterListFromConfig("./config.yml")
    print(character_list)
    for character in character_list:
        data = loadCharacterData(character)
        writeCharacterDataToFile(data, "./data/{}/".format(character))