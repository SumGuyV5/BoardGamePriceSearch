import time
from Modules.Games401 import Games401
from Modules.BoardGameBliss import BoardGameBliss
from Modules.MeepleMart import MeepleMart
from Modules.LegendsWarehouse import LegendsWarehouse
from Modules.WoodForSheep import WoodForSheep
from Modules.LvlupGames import LvlupGames


def search_results(search_for):
    start_time = time.time()
    html = ""
    stores = [BoardGameBliss(search_for), Games401(search_for), MeepleMart(search_for), LegendsWarehouse(search_for),
              WoodForSheep(search_for), LvlupGames(search_for)]
    for store in stores:
        store.search()
    for store in stores:
        html += str(store.results(4))
    print(f"Search of Board Games took {time.time() - start_time} to run")
    return html
