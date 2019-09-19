import urllib.request
import json
import time

link = 'https://www.reddit.com/r/todayilearned/new/.json'

news=[]

def get_news(link):
	"""
	Getting post from https://www.reddit.com/r/todayilearned/new and saving it in "news" list and sorted it by oldest to newest in "news2" list.
	"""
	global newest
	global news2
	with urllib.request.urlopen(link) as f:
		data_til = json.load(f)
	for i in range(len(data_til['data']['children'])):
		fact = data_til['data']['children'][i]['data']['title']
		if fact[:3] == 'TIL' and fact[:8] == 'TIL that':
			fact = '>'+fact[9].upper()+fact[10:]
		if fact[:3] == 'TIL':
			fact = '>'+fact[4].upper()+fact[5:]
		#print(type(news))
		link = data_til['data']['children'][i]['data']['url']
		news.append([fact,link])
		newest = news[0][0]
	x = 0 - len(news)
	news2 = news[::-1]
	
def save_news():
	"""
	Saving news to file TIL.txt
	"""
	output = open('TIL.txt', 'w')
	for i in range(len(news2)):
		output.write(news2[i][0])
		output.write('\n')
		output.write(news2[i][1])
		output.write('\n\n')
	output.close()
	
	
def print_news():
	"""
	Printing news in console
	"""
	for i in range(len(news2)):
		print(news2[i][0])
		print(news2[i][1])
		print('\n')

def new_news(link,newest):
	"""
	Checking is new news appered, if so print it in console and save to file
	"""
	while True:
		time.sleep(60)
		# Catching possible HTTP errors
		try:
			with urllib.request.urlopen(link) as f:
				data_til = json.load(f)
		except:
			print('\nSomething went wrong')
			continue
		fact = data_til['data']['children'][0]['data']['title']
		if fact[:3] == 'TIL' and fact[:8] == 'TIL that':
			fact = '>'+fact[9].upper()+fact[10:]
		if fact[:3] == 'TIL':
			fact = '>'+fact[4].upper()+fact[5:]
		if fact != newest:
			link = data_til['data']['children'][0]['data']['url']
			output = open('TIL.txt', 'a')
			print('\n',fact,sep='')
			print(link)
			output.write('New fact!\n')
			output.write(fact)
			output.write('\n')
			output.write(link)
			output.write('\n')
			newest = fact
			output.close()
		else:
			print('There is no new facts.')
					
get_news(link)
print_news()
save_news()
new_news(link,newest)


