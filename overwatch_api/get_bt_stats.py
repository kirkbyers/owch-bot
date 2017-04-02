import requests
from bs4 import BeautifulSoup

def convertBt(battleTag):
  '''Convert battleTag from # to -'''
  convertedTag = battleTag.translate({ord('#'):'-'})
  return convertedTag

def buildApiURL(region, battleTag):
  baseURL = 'https://playoverwatch.com/en-us/career/pc'
  requestURL = baseURL + '/' + region + '/' + battleTag
  return requestURL

def getStats(battleTag):
  convertedTag = convertBt(battleTag)
  requestsURL = buildApiURL('us', convertedTag)
  r = requests.get(requestsURL)

  # Handles errors
  if r.status_code == 404:
    return {'error': 404}

  soup = BeautifulSoup(r.text, 'html5lib')

  # Get a list of all played heros in comp
  compHeros = soup.select('div#competitive section.career-stats-section select[data-js="career-select"] option')
  playedHeros = []
  for hero in compHeros:
    playedHeros.append({
      'name': hero.get_text(),
      'id': hero.attrs.get('value')
    })
  
  # Get stats
  heroStats = {}
  for hero in playedHeros:
    heroStats[hero['name']] = {}
    statRows = soup.select('div#competitive section.career-stats-section div[data-category-id="' + hero['id'] + '"] table tbody tr')
    for stat in statRows:
      statName = stat.contents[0].get_text()
      statValue = stat.contents[1].get_text()
      heroStats[hero['name']][statName] = statValue
  
  return heroStats