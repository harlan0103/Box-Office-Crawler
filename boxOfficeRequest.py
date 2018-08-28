"""
Usage:
	boxOfficeRequest [-dow]

Options:
	-d 		All time domestic box-office
	-o 		All time worldwide box-office
	-w		Weekend box-office
"""

import requests
from bs4 import BeautifulSoup
from docopt import docopt
from prettytable import PrettyTable

def domestic():
	#Get url address of boxofficemojo.com
	res = requests.get('http://www.boxofficemojo.com/alltime/domestic.htm')
	soup = BeautifulSoup(res.text, 'lxml')

	#Get movie details by resolving html tags from soup object
	movieInfo = soup.select('div[id=body] > table > tr > td > center > table > tr > td > table > tr > td > font')

	"""
	#1 Rank
	#2 Title
	#3 Studio
	#4 Lifetime gross
	#5 Year
	"""	
	title = []
	domesticGross = []
	year = []
	rank = []
	#For each time getting movie data, we first delete all rows in table
    #cur.execute('DELETE FROM domestic')

	#Append movie detials into created array
	for i in movieInfo:
		if movieInfo.index(i)%5 is 0:
			rank.append(i.get_text())
		elif movieInfo.index(i)%5 is 1:
			title.append(i.get_text())
		elif movieInfo.index(i)%5 is 3:
			domesticGross.append(i.get_text())
		elif movieInfo.index(i)%5 is 4:
			year.append(i.get_text())

	#Create table with field name
	ptable = PrettyTable(["Rank", "Movie Name", "Lifetime Gross", "Year"])
	#Iterate each movie item and add to the table
	for i in range(1,101):
		ptable.add_row([rank[i],title[i],domesticGross[i],year[i]])

	print(ptable)

def main():
	arguments = docopt(__doc__)

	#Get arguments information and call method based on argument
	if arguments['-d'] is True:
		domestic()
	elif arguments['-o'] is True:
		print("worldwide")
	elif arguments['-w'] is True:
		print("weekend")

if __name__ == "__main__":	
	main()	