from Modules.Games401 import Games401
from Modules.BoardGameBliss import BoardGameBliss
from Modules.MeepleMart import MeepleMart
from Modules.LegendsWarehouse import LegendsWarehouse
from Modules.WoodForSheep import WoodForSheep
from Modules.LvlupGames import LvlupGames


def search_results(search_for):
    html = ""
    stores = [BoardGameBliss(search_for), Games401(search_for), MeepleMart(search_for), LegendsWarehouse(search_for),
              WoodForSheep(search_for), LvlupGames(search_for)]
    for store in stores:
        html += str(store.results(4))
    return html

