from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.rottentomatoes.com/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, 'html.parser')

films = []
titles = []
scores = []

# take films from Top Box Office part of the website
for article in content.findAll('table', attrs={'class': 'movie_list', 'id': 'Top-Box-Office'}):
	#middle_col contain title of the movie
	for film in article.findAll('td', attrs={'class': 'middle_col'}):
		title = film.text.strip()
		titles.append(title)
	#left_col contain score (in percents) of the movie
	for film in article.findAll('td', attrs={'class': 'left_col'}):
		score = film.text.strip()
		scores.append(score)
	
#creating list of dictionaries with details(title,score) about movies
for i in range(len(titles)):
	filmObject = {
		'title' : titles[i],
		'score' : scores[i]
	}
	films.append(filmObject)

#saving list in json format
with open('filmsData.json', 'w') as outfile:
	json.dump(films, outfile)
	
#writing data from json file
with open('filmsData.json') as json_data:
	jsonData = json.load(json_data)
	
#printing in console
print('Top Box Office movies:')
for i in jsonData:
	print('\nTitle:',i['title'])
	print('Score:',i['score'])