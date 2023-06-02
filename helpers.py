from typing import List

from hero import HeroInfo
from game import GameInfo

def get_hero_stat(urls: List['str']) -> dict:
    result = {}
    for url in urls:
        temp_heros = HeroInfo(url)
        for hero in temp_heros.heros:
            temp_hero = result.get(hero.name)
            if temp_hero:
                temp_hero.win += hero.win
                temp_hero.allGame += hero.allGame
            else:
                result[hero.name] = hero

    for hero in result.values():
        hero.setWinRateAndWeight()

    return result


def get_game_stat(regions: List[tuple], heros: get_hero_stat) -> dict:
    result = {}
    for region in regions:
        temp_games = GameInfo(region[1], heros)
        count_game = len(temp_games.games)
        my_win_rate = 0

        for game in temp_games.games:
            if game.winner == game.predict:
                my_win_rate += 1

        result[region[0]] = my_win_rate / count_game

    return result
