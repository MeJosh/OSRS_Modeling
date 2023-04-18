import requests
from bs4 import BeautifulSoup

def get_item_data(url):
    page = requests.get(url)
    if page.status_code != 200:
        print(f"[ERROR] Unable down load item page: {url}")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(class_="infobox-bonuses")

    if len(results) == 0:
        print(f"[ERROR] Unable to find info-bonuses for {url}")
        return None

    infobox = results[0]
    if len(infobox) > 1:
        print(f"[WARNING] Found multiple info-bonuses for {url}")

    # There should only be one of these
    for result in results:
        item_data = format_item_data(url, result)
        print(item_data)

def get_monster_data(url):
    page = requests.get(url)
    if page.status_code != 200:
        print(f"[ERROR] Unable down load monster page: {url}")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(class_="infobox-monster")

    if len(results) == 0:
        print(f"[ERROR] Unable to find an info-monster for {url}")
        return None

    infobox = results[0]
    if len(infobox) > 1:
        print(f"[WARNING] Found multiple info-monster for {url}")

    # There should only be one of these
    for result in results:
        monster_data = format_monster_data(url, result)
        print(monster_data)



def format_item_data(url, infobox_html):
    item_data = {}
    item_data["url"] = url

    item_data["bonuses"] = {}
    rows = infobox_html.find_all('tr')

    attack_stats_html = rows[3]
    attack_bonuses = [element.contents for element in attack_stats_html.find_all("td")]
    if len(attack_bonuses) != 5:
        print(f"[WARNING] Unable to find attack bonuses for {url}")
    attack_bonuses = [int(bonus[0].replace("+", "")) for bonus in attack_bonuses]
    item_data["bonuses"]["attack_stab"] = attack_bonuses[0]
    item_data["bonuses"]["attack_slash"] = attack_bonuses[1]
    item_data["bonuses"]["attack_crush"] = attack_bonuses[2]
    item_data["bonuses"]["attack_magic"] = attack_bonuses[3]
    item_data["bonuses"]["attack_ranged"] = attack_bonuses[4]

    defense_stats_html = rows[8]
    defense_bonuses = [element.contents for element in defense_stats_html.find_all("td")]
    if len(defense_bonuses) != 5:
        print(f"[WARNING] Unable to find defense bonuses for {url}")
    defense_bonuses = [int(bonus[0].replace("+", "")) for bonus in defense_bonuses]
    item_data["bonuses"]["defense_stab"] = defense_bonuses[0]
    item_data["bonuses"]["defense_slash"] = defense_bonuses[1]
    item_data["bonuses"]["defense_crush"] = defense_bonuses[2]
    item_data["bonuses"]["defense_magic"] = defense_bonuses[3]
    item_data["bonuses"]["defense_ranged"] = defense_bonuses[4]

    defense_stats_html = rows[8]
    defense_bonuses = [element.contents for element in defense_stats_html.find_all("td")]
    if len(defense_bonuses) != 5:
        print(f"[WARNING] Unable to find defense bonuses for {url}")
    defense_bonuses = [int(bonus[0].replace("+", "")) for bonus in defense_bonuses]
    item_data["bonuses"]["defense_stab"] = defense_bonuses[0]
    item_data["bonuses"]["defense_slash"] = defense_bonuses[1]
    item_data["bonuses"]["defense_crush"] = defense_bonuses[2]
    item_data["bonuses"]["defense_magic"] = defense_bonuses[3]
    item_data["bonuses"]["defense_ranged"] = defense_bonuses[4]

    other_stats_html = rows[13]
    other_bonuses = [element.contents for element in other_stats_html.find_all("td")]
    if len(other_bonuses) != 5:
        print(f"[WARNING] Unable to find other bonuses for {url}")

    slot_type = other_bonuses[4]
    print(slot_type)

    other_bonuses = [bonus[0].replace("+", "") for bonus in other_bonuses[:4]]
    other_bonuses = [bonus.replace("%", "") for bonus in other_bonuses]
    item_data["bonuses"]["melee_strength"] = int(other_bonuses[0])
    item_data["bonuses"]["ranged_strength"] = int(other_bonuses[1])
    item_data["bonuses"]["magic_damage"] = int(other_bonuses[2])
    item_data["bonuses"]["prayer_bonus"] = int(other_bonuses[3])

    return item_data

def format_monster_data(url, infobox_html):
    errors = []
    monster_data = {}
    monster_data["url"] = url

    rows = infobox_html.find_all('tr')

    # Find the Monster Name
    monster_header = infobox_html.find_all(class_="infobox-header")
    if len(monster_header) == 1:
        monster_data["name"] = monster_header[0].contents
    else:
        errors.push(f"[ERROR] Expected exactly one 'infobox-header' class, but instead found {len(monster_header)}")


    # Find the Monster Combat Info
    for i in range(0, len(rows)):
        row = rows[i]
        #print(row.prettify())

    return monster_data

if __name__ == "__main__":
    #get_monster_data("https://oldschool.runescape.wiki/w/King_Black_Dragon")
    get_item_data("https://oldschool.runescape.wiki/w/Rune_platebody")