import requests
from bs4 import BeautifulSoup


class HerosInfo:
    def __init__(self, url: str):
        self.url = url
        self.dict_hero = {}
        self._parse_data()

    def get_hero_info(self, name: str):
        return self.dict_hero.get(name)

    def _parse_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'lxml')

        for row in soup.find_all('tr', class_='dota-stat-row'):
            tds = row.find_all('td')
            name = tds[1].find_all('a')[1].get('title')

            win = int(tds[3].text)
            lose = int(tds[4].text)
            all_game = win + lose
            if all_game != 0:
                win_rate = (win / all_game) * 100
            else:
                win_rate = 0
            weight = win_rate * all_game

            self.dict_hero[name] = {
                'name': name,
                'win': win,
                'lose': lose,
                'all': all_game,
                'win_rate': win_rate,
                'weight': weight
            }

    def __repr__(self):
        return f'heros: {self.dict_hero}'


class GamesInfo:
    def __init__(self, url, heros: HerosInfo):
        self.url = url
        self.heros_info = heros
        self.list_games = []
        self._parseData()
        self._setPredict()

    def __len__(self):
        return len(self.list_games)

    def getListGames(self):
        return self.list_games

    def _parseData(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'lxml')

        events = soup.find_all('div', class_='brkts-popup brkts-match-info-popup')
        for event in events:
            names = event.find_all('span', class_='name')

            first_team = names[0].text
            second_team = names[1].text

            games = event.find_all('div', class_='brkts-popup-body-element brkts-popup-body-game')
            for game in games:
                picks = game.find_all('div', class_='brkts-popup-body-element-thumbs')

                first_pick = list(map(lambda x: x.get('title'), picks[0].find_all('a')))
                second_pick = list(map(lambda x: x.get('title'), picks[1].find_all('a')))

                if not first_pick or not second_pick:
                    continue

                img = game.find('div', class_='brkts-popup-spaced').find('img').get('src')
                if img.__contains__('NoCheck.png'):
                    winner = second_team
                else:
                    winner = first_team

                self.list_games.append(
                    {
                        'first team': first_team,
                        'second team': second_team,
                        'first team pick': first_pick,
                        'second team pick': second_pick,
                        'winner': winner,
                    }
                )

    def _setPredict(self):
        for game in self.list_games:
            first_pick = 0
            second_pick = 0
            for i in range(5):
                first_pick += self.heros_info.get_hero_info(game['first team pick'][i])['weight']
                second_pick += self.heros_info.get_hero_info(game['second team pick'][i])['weight']

            if first_pick >= second_pick:
                game['predict'] = game['first team']
            else:
                game['predict'] = game['second team']
