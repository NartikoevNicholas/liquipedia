import requests

from typing import List

from bs4 import BeautifulSoup


class Game:
    def __init__(
            self,
            first_team: str,
            second_team: str,
            first_team_pick: List['str'],
            second_team_pick: List['str'],
            winner: str
    ):
        self._firstTeam = first_team
        self._secondTeam = second_team
        self._firstTeamPick = first_team_pick
        self._secondTeamPick = second_team_pick
        self._winner = winner
        self._predict = None

    @property
    def winner(self):
        return self._winner

    @property
    def predict(self):
        return self._predict

    def setPredict(self, heros: dict):
        first_pick = 0
        second_pick = 0
        for i in range(5):
            first_pick += heros[self._firstTeamPick[i]].weight
            second_pick += heros[self._secondTeamPick[i]].weight

        if first_pick >= second_pick:
            self._predict = self._firstTeam
        else:
            self._predict = self._secondTeam


class GameInfo:
    def __init__(self, url: str, heros: dict):
        self._games = []
        self._parseData(url, heros)

    @property
    def games(self) -> List[Game]:
        return self._games

    def _parseData(self, url, heros):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        events = soup.find_all('div', class_='brkts-popup brkts-match-info-popup')
        for event in events:
            names = event.find_all('span', class_='name')

            first_team = names[0].text
            second_team = names[1].text

            games = event.find_all('div', class_='brkts-popup-body-element brkts-popup-body-game')
            for game in games:
                picks = game.find_all('div', class_='brkts-popup-body-element-thumbs')

                first_team_pick = list(map(lambda x: x.get('title'), picks[0].find_all('a')))
                second_team_pick = list(map(lambda x: x.get('title'), picks[1].find_all('a')))

                if not first_team_pick or not second_team_pick:
                    continue

                img = game.find('div', class_='brkts-popup-spaced').find('img').get('src')
                if img.__contains__('NoCheck.png'):
                    winner = second_team
                else:
                    winner = first_team

                self._games.append(
                    Game(
                        first_team=first_team,
                        second_team=second_team,
                        first_team_pick=first_team_pick,
                        second_team_pick=second_team_pick,
                        winner=winner
                    )
                )
                self._games[-1].setPredict(heros)
