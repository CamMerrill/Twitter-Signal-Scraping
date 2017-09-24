from bs4 import BeautifulSoup
import requests

locale = raw_input("global or united-states: ")
accountType = raw_input("What area: brands, celebrities, community, entertainment, media, place, society, sport: ")

outputFile = open("Clean/" + str(locale) + "-" + str(accountType), 'w')


handleList = []
go = True
urlI = 1
urlJ = 5
#first 50
while go:


	url = "https://www.socialbakers.com/statistics/twitter/profiles/united-states/brands/page-"
	url = "https://www.socialbakers.com/statistics/twitter/profiles/"
	url += str(locale) + "/" + str(accountType) + "/page-"
	url += str(urlI) + "-"
	url += str(urlJ) + "/"
	req = requests.get(url)
	data = req.text
	soup = BeautifulSoup(data, "html.parser")
	mydivs = soup.findAll("td", { "class" : "name" })

	for item in mydivs:

		line = str(item)
		ogLine = line
		startAt = line.find("(@")
		line = line[startAt:]
		endAt = line.find(")")
		line = line[:endAt]
		handle = line[2:]
		if handle not in handleList:
			handleList.append(handle)
	if urlJ == 100:
		go = False
	
	urlI += 1
	urlJ += 1
	print urlJ
	print len(handleList)

for item in handleList:
	outputFile.write(item+"\n")
	print item
