import requests
from bs4 import BeautifulSoup

def get_monster_data(url):
    page = requests.get(url)
    if page.status_code != 200:
        print(f"[ERROR] Unable down load monster page: {url}")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(class_="infobox-monster")
    
    if len(infobox) == 0:
        print(f"[ERROR] Unable to find an info-monster for {url}")
        return None
    
    infobox = results[0]
    if len(infobox) > 1:
        print(f"[WARNING] Found multiple info-monster for {url}")

    # There should only be one of these
    for result in results:
        print(result.prettify())


if __name__ == "__main__":
    get_monster_data("https://oldschool.runescape.wiki/w/King_Black_Dragon")