from helpers import get_hero_stat, get_game_stat


host = 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/'

hero_stat_url = [
    f'{host}Eastern_Europe/Statistics/Division_I',
    # f'{host}China/Statistics/Division_I',
    # f'{host}Western_Europe/Statistics/Division_I',
    # f'{host}North_America/Statistics/Division_I',
    # f'{host}South_America/Statistics/Division_I',
    # f'{host}Southeast_Asia/Statistics/Division_I'
]

game_stat_url = [
    # ('Eastern Europe', f'{host}Eastern_Europe/Division_I'),
    # ('China', f'{host}China/Division_I'),
    ('Western Europe', f'{host}Western_Europe/Division_I'),
    # ('North America', f'{host}North_America/Division_I'),
    # ('South America', f'{host}North_America/Division_I'),
    # ('Southeast Asia', f'{host}Southeast_Asia/Division_I')
]

hero_stat = get_hero_stat(hero_stat_url)

game_stat = get_game_stat(game_stat_url, hero_stat)

print(game_stat)
