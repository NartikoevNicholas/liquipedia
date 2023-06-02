from hero import HerosInfo, GamesInfo

list_regions = [
    {
        'name': 'Eastern Europe',
        'statistic_hero_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/Eastern_Europe/Statistics/Division_I',
        'all_game_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/Eastern_Europe/Division_I'
    },
    {
        'name': 'China',
        'statistic_hero_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/China/Statistics/Division_I',
        'all_game_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/China/Division_I'
    },
    {
        'name': 'Western Europe',
        'statistic_hero_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/Western_Europe/Statistics/Division_I',
        'all_game_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/Western_Europe/Division_I'
    },
    {
        'name': 'North America',
        'statistic_hero_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/North_America/Statistics/Division_I',
        'all_game_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/North_America/Division_I'
    },
    {
        'name': 'South America',
        'statistic_hero_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/South_America/Statistics/Division_I',
        'all_game_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/South_America/Division_I'
    },
    {
        'name': 'Southeast Asia',
        'statistic_hero_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/Southeast_Asia/Statistics/Division_I',
        'all_game_url': 'https://liquipedia.net/dota2/Dota_Pro_Circuit/2023/3/Southeast_Asia/Division_I'
    }
]

for region in list_regions:
    heros = HerosInfo(region['statistic_hero_url'])
    games = GamesInfo(region['all_game_url'], heros)

    wr = 0
    for game in games.getListGames():
        if game['winner'] == game['predict']:
            wr += 1

    print(f'{region["name"]}:{wr / len(games) * 100}')
