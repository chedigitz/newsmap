# import modules
import urllib2
import csv

# set standard variables

site = urllib2.urlopen('http://www.cnn.com/')
html = site.read()
start = 0
end = 0
links = []
keys = []
outdata =[]

#import .csv data

with open('/Users/joereidl/code/newsmap/Keyword List - Sheet1.csv','r') as keylist:
	keywords = csv.reader(keylist)
	for x in keywords:
		keys.append(x[0])

# finds all links on page

while start != -1:
	start = html.find('a href="',end) #finds start of '<a href="' tags
	end = html.find('"', start + 8)
	ltexts = html.find('>',end) #finds start of link text
	ltexte = html.find('</a>',end) #finds end of '<a href="' tags
	linktext = html[ltexts + 1:ltexte]
	links.append([linktext,html[start + 8:end]]) #adds links to a list
	start = html.find('a href="', end + 1)

#check list of keys against the list of links

for x in links:
	for y in keys:
		if y in x[0]:
			outdata.append([x,y])
			
for x in outdata:
	print x