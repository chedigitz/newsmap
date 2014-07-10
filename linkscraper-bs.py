# import modules
import urllib2
import csv
from bs4 import BeautifulSoup
import nltk
# set standard variables

site = urllib2.urlopen('http://www.cnn.com/')
html2 = site.read()
htmlbody = BeautifulSoup(html2)

link_text = []


# retrieves LIST Of keywords from a filepath string that points to csv
def getKeyWordListfromCSV(filePath):
	magicKeys = []
	with open(filePath,'r') as keylist:
		keywords = csv.reader(keylist)
		for x in keywords:
			magicKeys.append(x[0])

	return magicKeys



# function for filtering list of words and returning true if its a match
def filterTextForKeyWords(listOfWords, listofKeywords):
	for word in listOfWords:
		for keyWord in listofKeywords:
			if word==keyWord:
				return True



keys = getKeyWordListfromCSV('data/Keyword List - Sheet1.csv')
results = []

for link in htmlbody.find_all('a'):
	tempText =  link.get_text()
	tokenWords = nltk.word_tokenize(tempText)
	print tempText
	print tokenWords
	if len(tokenWords) != 0:
		print "we have a hit"
		print link
		if filterTextForKeyWords(tokenWords,keys):
			print "awesome it matches our magic words"
			results.append(link)


# start = 0
# end = 0
# links = []
keys = []
# outdata =[]

# #import .csv data
print "total links found"
print len(htmlbody.find_all('a'))
print "Total links that match"
print len(results)



# # #check list of keys against the list of links
# for x in link_text:
# 	for y in keys:
# 		if y in x[0]:
# 			outdata.append([x,y])


# # finds all links on page

# while start != -1:
# 	start = html2.find('a href="',end) #finds start of '<a href="' tags
# 	end = html2.find('"', start + 8)
# 	ltexts = html2.find('>',end) #finds start of link text
# 	ltexte = html2.find('</a>',end) #finds end of '<a href="' tags
# 	linktext = html2[ltexts + 1:ltexte]
# 	links.append([linktext,html2[start + 8:end]]) #adds links to a list
# 	start = html2.find('a href="', end + 1)


			
for x in results:
	print x		