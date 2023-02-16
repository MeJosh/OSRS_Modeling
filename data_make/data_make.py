import requests
from bs4 import BeautifulSoup


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
    get_monster_data("https://oldschool.runescape.wiki/w/King_Black_Dragon")