import requests
from bs4 import BeautifulSoup
from getScores import getScores
from getOPS import getOPS
import sys
from datetime import date

today = str(date.today())
year = int(today[0:4])

validDate = False
'''
while(not validDate):
    today = input("Enter a date (YYYY-MM-DD) -> ")
    if(int(today[0:4]) < 2011 or int(today[0:4]) > 2019):
        print("Invalid date! Try again.")
    else:
        year = int(today[0:4])
        validDate = True
'''

url = 'https://www.baseballpress.com/lineups/{}'.format(today)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

players_to_delete = soup('span', class_='mobile-name')
if players_to_delete:
    for i in players_to_delete:
        i.extract()

players = soup('a', class_='player-link')
teams = soup('a', class_='mlb-team-logo bc')

for i in range(len(players)):
    players[i] = players[i].get_text()

for i in range(len(teams)):
    teams[i] = teams[i].get_text().strip().lower()


validInput = False
while(not validInput):
    if(len(teams) == 0):
        print("No games played that day.")
        sys.exit()
    gameName = input("Enter team name: ").lower()
    if(gameName not in teams):
        print("Invalid team name! Try again.")
    else:
        gameNum = int(teams.index(gameName) / 2)
        validInput = True

awayTeam = teams[gameNum*2]
homeTeam = teams[gameNum*2+1]
start = gameNum * 20
finish = start + 20

away_pitcher = players[start]
home_pitcher = players[start+1]

away_lineup = players[start+2:start+11]
home_lineup = players[start+11:finish]

awayScore, homeScore = getScores(awayTeam, homeTeam, today)
away_OPS = [0] * 9
home_OPS = [0] * 9

for i in range(len(away_lineup)):
    away_OPS[i] = getOPS(away_lineup[i], str(year-1))

for i in range(len(home_lineup)):
    home_OPS[i] = getOPS(home_lineup[i], str(year-1))

print("\n%%% {} (A) %%%".format(awayTeam.capitalize()))
for i in range(len(away_lineup)):
    print("{}. {}, {}".format(i+1, away_lineup[i], away_OPS[i]))
print("P. {}".format(away_pitcher))

print("\n%%% {} (H) %%%".format(homeTeam.capitalize()))

for i in range(len(home_lineup)):
    print("{}. {}, {}".format(i+1, home_lineup[i], home_OPS[i]))
print("P. {}".format(home_pitcher))

print("\n{}: {}".format(awayTeam.capitalize(), awayScore))
print("{}: {}".format(homeTeam.capitalize(), homeScore))
