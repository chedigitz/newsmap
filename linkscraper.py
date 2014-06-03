# import modules
import urllib2

# set standard variables

site = urllib2.urlopen('http://www.cnn.com/')
html = site.read()
start = 0
end = 0
links = []

# finds all links on page

while start != -1:
	start = html.find('a href="',end) #finds start of '<a href="' tags
	end = html.find('"', start + 8)
	ltexts = html.find('>',end) #finds start of link text
	ltexte = html.find('</a>',end) #finds end of '<a href="' tags
	linktext = html[ltexts + 1:ltexte]
	links.append([linktext,html[start + 8:end]]) #adds links to a list
	start = html.find('a href="', end + 1)
	
for x in links:
	print x