import urllib.request
import json
import webbrowser
import time

wiki_random = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json'

with urllib.request.urlopen(wiki_random) as f:
	data_wiki_random = json.load(f)

while True:
	wiki_random = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json'

	with urllib.request.urlopen(wiki_random) as f:
		data_wiki_random = json.load(f)
	title = data_wiki_random['query']['random'][0]['title']
	print('\nDo you want to read about', title, '?')
	t = input('(Type "yes" to open article)> ')
	if t == 'yes':
		link = 'https://en.wikipedia.org/wiki?curid='+str(data_wiki_random['query']['random'][0]['id'])
		webbrowser.open(link)
	print('\nDo you want new article?')
	t = input('\n(yes/no)> ')
	if t == 'yes':
		print('Searching for the new article...')
		time.sleep(3)
		continue
	if t == 'no': break
		
	
