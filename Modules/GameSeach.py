from Modules.Games401 import Games401
from Modules.BoardGameBliss import BoardGameBliss
from Modules.MeepleMart import MeepleMart
from Modules.LegendsWarehouse import LegendsWarehouse
from Modules.WoodForSheep import WoodForSheep
from Modules.LvlupGames import LvlupGames

def search_results(search):
    rtn = ""
    searches = [BoardGameBliss(search), Games401(search), MeepleMart(search), LegendsWarehouse(search),
                WoodForSheep(search), LvlupGames(search)]
    for search in searches:
        rtn += str(search.results(4))
    return rtn

