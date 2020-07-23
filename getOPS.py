import requests
from bs4 import BeautifulSoup

#name = input("Enter name -> ").lower()
#first, last = name.split(" ")

def getOPS(name, year):
    name = name.strip().lower()
    first, last = name.split(' ')[:2]
    url = 'https://www.baseball-reference.com/players/{}/{}{}01.shtml'.format(last[0], last[:5], first[:2])

    print(url)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    years_to_delete = soup('tr', class_='minors_table hidden')
    if years_to_delete:
        for i in years_to_delete:
            i.extract()

    years_raw = soup('th', {'data-stat' : 'year_ID'})
    ops = soup('td', {'data-stat' : 'onbase_plus_slugging_plus'})

    for i in range(len(ops)):
        ops[i] = ops[i].get_text()

    for i in range(len(years_raw)):
        years_raw[i] = years_raw[i].get_text()

    years = []
    [years.append(x) for x in years_raw if x not in years] 

    ops = list(filter(None, ops))
    years = list(filter(None, years))

    try:
        pairedOPS = {years[i]: ops[i-1] for i in range(len(years))}
    except:
        pass

    try:
        returnOPS = pairedOPS[year]
    except:
        returnOPS = 0
    return(returnOPS)
