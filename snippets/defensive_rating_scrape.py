from bs4 import BeautifulSoup
from urllib2 import urlopen
import pickle
import re


URL_BASE ="http://www.basketball-reference.com/leagues/NBA_{}_ratings.html"
start_year = 1997
new_file_path = ('../data/defensive_ratings_adjusted.pkl')

team_map = {
    u'Toronto Raptors': 'TOR',
    u'Brooklyn Nets': 'BKN',
    u'New Jersey Nets': 'NJN',
    u'Boston Celtics': 'BOS',
    u'New York Knicks': 'NYK',
    u'Philadelphia 76ers': 'PHI',
    u'Chicago Bulls': 'CHI',
    u'Cleveland Cavaliers': 'CLE', 
    u'Milwaukee Bucks': 'MIL', 
    u'Indiana Pacers': 'IND', 
    u'Detroit Pistons': 'DET', 
    u'Atlanta Hawks': 'ATL', 
    u'Washington Wizards': 'WAS', 
    u'Washington Bullets': 'WAS', 
    u'Miami Heat': 'MIA', 
    u'Orlando Magic': 'ORL', 
    u'Charlotte Hornets': 'CHA', 
    u'Charlotte Bobcats': 'CHA', 
    u'Portland Trail Blazers': 'POR', 
    u'Oklahoma City Thunder': 'OKC', 
    u'Denver Nuggets': 'DEN', 
    u'Utah Jazz': 'UTA', 
    u'Minnesota Timberwolves': 'MIN', 
    u'Golden State Warriors': 'GSW', 
    u'Los Angeles Clippers': 'LAC', 
    u'Phoenix Suns': 'PHX', 
    u'Sacramento Kings': 'SAC', 
    u'Los Angeles Lakers': 'LAL', 
    u'Memphis Grizzlies': 'MEM', 
    u'Houston Rockets': 'HOU', 
    u'Dallas Mavericks': 'DAL', 
    u'San Antonio Spurs': 'SAS', 
    u'New Orleans Pelicans': 'NOP',
    u'New Orleans/Oklahoma City Hornets': 'NOP',
    u'New Orleans Hornets': 'NOH',
    u'Vancouver Grizzlies': 'VAN',
    u'Seattle SuperSonics': 'SEA'
}

defensive_stats = []

for i in range(0, 20):
    team_defensive_ratings_adjusted = {}
    year = start_year + i
    html = urlopen(URL_BASE.format(year)).read()
    soup = BeautifulSoup(html, "lxml")
    rows = soup.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if not columns:
            continue
        team_name = columns[0].get_text()
        adjusted_defensive_rating = columns[12].get_text()
        if team_name == u'New Orleans/Oklahoma City Hornets':
            print team_map[team_name]
            input()
        team_defensive_ratings_adjusted[team_map[team_name]] = float(adjusted_defensive_rating)
        print "{}-{} {}: {}".format(year-1, year, team_name, adjusted_defensive_rating)
    defensive_stats.append(team_defensive_ratings_adjusted)


print defensive_stats
with open(new_file_path, "wb") as output_file:
    pickle.dump(defensive_stats, output_file)
    




