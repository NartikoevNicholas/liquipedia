import requests

from typing import List

from bs4 import BeautifulSoup


class Hero:
    def __init__(self, name: str, win: int, all_game: int):
        self._name = name
        self._win = win
        self._allGame = all_game
        self._winRate = None
        self._weight = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def win(self) -> int:
        return self._win

    @win.setter
    def win(self, value):
        self._win = value

    @property
    def allGame(self) -> int:
        return self._allGame

    @allGame.setter
    def allGame(self, value):
        self._allGame = value

    @property
    def winRate(self):
        return self._winRate

    @property
    def weight(self):
        return self._weight

    def setWinRateAndWeight(self):
        if self._allGame:
            self._winRate = self._win / self._allGame * 100
        else:
            self._winRate = 0
        self._weight = self._winRate * self._allGame


class HeroInfo:
    def __init__(self, url: str):
        self._heros = []
        self._parse_data(url)

    @property
    def heros(self) -> List[Hero]:
        return self._heros

    def _parse_data(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        for row in soup.find_all('tr', class_='dota-stat-row'):
            tds = row.find_all('td')
            self._heros.append(
                Hero(
                    name=tds[1].find_all('a')[1].get('title'),
                    win=int(tds[3].text),
                    all_game=int(tds[2].text)
                )
            )
