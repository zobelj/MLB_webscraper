import requests
from bs4 import BeautifulSoup

def getScores(awayTeam, homeTeam, date):
    url = 'https://www.mlb.com/scores/{}'.format(date)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    teams = soup(class_='sc-elJkPf cPMFTM')
    runsA = soup(class_='sc-fBuWsC jZvFDL')
    runsH = soup(class_='sc-fBuWsC wPDPl')

    runs = [0] * (len(runsA * 2))

    for i in range(len(runsA)):
        runs[2*i] = runsA[i]
        runs[2*i+1] = runsH[i]

    for i in range(len(teams)):
        teams[i] = teams[i].get_text().lower()

    for i in range(len(runs)):
        runs[i] = runs[i].get_text()

    scores = {teams[i]: runs[i] for i in range(len(runs))}

    try:
        awayScore = scores[awayTeam]
    except:
        print('Error getting away team score!')
        awayScore = 0

    try:
        homeScore = scores[homeTeam]
    except:
        print('Error getting home team score!')
        homeScore = 0

    return(awayScore, homeScore)
