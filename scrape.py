import requests
from bs4 import BeautifulSoup
## input
# set url
url = 'https://www.pcso.gov.ph/SearchLottoResult.aspx'


## f1 start
# get the html of the url
page = requests.get(url)

# parse the html using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# store the html table
pre_table = soup.find_all('table', attrs={'class':'Grid'})[0]

# gets all the rows of the table
table = pre_table.find_all('tr')
## f1 end

## f2 start
# empty array for table data
td = []

# number of rows
length = len(table)

# selects certain LOTTO GAMES
for i in range(1,length):
	if table[i].td.get_text() == "Superlotto 6/49":
		td.append(table[i].td.get_text())
		td.append(table[i].td.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.next_sibling.get_text())
	elif table[i].td.get_text() == "Ultra Lotto 6/58":
		td.append(table[i].td.get_text())
		td.append(table[i].td.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.next_sibling.get_text())
	elif table[i].td.get_text() == "Lotto 6/42":
		td.append(table[i].td.get_text())
		td.append(table[i].td.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.next_sibling.get_text())
	elif table[i].td.get_text() == "Grand Lotto 6/55":
		td.append(table[i].td.get_text())
		td.append(table[i].td.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.next_sibling.get_text())
	elif table[i].td.get_text() == "Megalotto 6/45":
		td.append(table[i].td.get_text())
		td.append(table[i].td.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.get_text())
		td.append(table[i].td.next_sibling.next_sibling.next_sibling.next_sibling.get_text())
## f2 end

## f3 start
grouped = []

for i in range (1,int((len(td)/5))+1):
	temp = []
	for j in range(0,5):
		temp.append(td.pop(0))
	grouped.append(temp)

game = input()

def game_select(game_name, result):
	if game_name == "6/49":
		for i in result:
			for j in i:
				if j == "Superlotto 6/49":
					return i
	elif game_name == "6/58":
		for i in result:
			for j in i:
				if j == "Ultra Lotto 6/58":
					return  i
	elif game_name == "6/42":
		for i in result:
			for j in i:
				if j == "Lotto 6/42":
					return  i
	elif game_name == "6/55":
		for i in result:
			for j in i:
				if j == "Grand Lotto 6/55":
					return  i
	elif game_name == "6/45":
		for i in result:
			for j in i:
				if j == "Megalotto 6/45":
					return  i
	else:
		return "Game not found."

lotto_game = game_select(game, grouped)

print("Lotto Game: "+ lotto_game[0])
print("Winning Combination: "+ lotto_game[1])
print("Date: "+ lotto_game[2])
print("Prize: "+ lotto_game[3])
print("Winners: "+ lotto_game[4])

## f3 end