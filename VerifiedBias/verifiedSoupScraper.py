from bs4 import BeautifulSoup
import requests

outputFile = open("soupOutput.txt", 'w')


handleList = []
go = True
url = "https://twitter.com/verified/following"
req = requests.get(url)
data = req.text
soup = BeautifulSoup(data, "html.parser")

print soup





