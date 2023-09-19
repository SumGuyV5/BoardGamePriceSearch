import time
from Modules.Games401 import Games401
from Modules.BoardGameBliss import BoardGameBliss
from Modules.MeepleMart import MeepleMart
from Modules.LegendsWarehouse import LegendsWarehouse
from Modules.WoodForSheep import WoodForSheep
from Modules.LvlupGames import LvlupGames
from bs4 import BeautifulSoup


def search_results(search_for, sites):
    start_time = time.time()
    soup = BeautifulSoup('<div class="grid-container"></div>', "html.parser")
    #soup2 = BeautifulSoup('<div><br/></div>', "html.parser")
    #label = soup2.new_tag('label', attrs={'class': 'checkbox'})
    #input = label.new_tag('input', attrs={'type': 'checkbox', 'name': 'sites',
    #                            'value': '401games', 'checked': 'checked'})
    #stores = [BoardGameBliss(search_for), Games401(search_for), MeepleMart(search_for), LegendsWarehouse(search_for),
    #          WoodForSheep(search_for), LvlupGames(search_for)]
    stores = []

    for site in sites:
        add = None
        if site == "boardgamebliss":
            add = BoardGameBliss(search_for)
        elif site == "401games":
            add = Games401(search_for)
        elif site == "meeplemart":
            add = MeepleMart(search_for)
        elif site == "legendswarehouse":
            add = LegendsWarehouse(search_for)
        elif site == "woodforsheep":
            add = WoodForSheep(search_for)
        elif site == "lvlupgames":
            add = LvlupGames(search_for)
        else:
            print("What the ?")

        if add is not None:
            stores.append(add)

    for store in stores:
        store.search()
    for store in stores:
        store.results(4, soup)
    print(f"Search of Board Games took {time.time() - start_time} to run")
    return str(soup)
