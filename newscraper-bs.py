import urllib2
import re
from bs4 import BeautifulSoup
import nltk

website = 'http://www.cnn.com/'
domslash = website.find('/',7)

def scraper(s):
	try:
		site = urllib2.urlopen(s)
		html = site.read()
		htmlbody = BeautifulSoup(html)
		# links = re.findall('<a href=".*?' + '.' + '</a>',html)
		links = htmlbody.find_all('a')
		# print links
		return links
	except:
		return 'Error loading site'
links2 = []
for x in scraper(website):
	# print x
	if x.has_key('href'):
 		links2.append(x['href'])

okCount = 0
brokenCount = 0
totalAnchors = 0 
for a in links2:
	print a
	totalAnchors = totalAnchors + 1
	if 'http://' not in a and '#' not in a:
		print '*****'
		print a
		print website[:domslash] + a
		try:
			site = urllib2.urlopen(website[:domslash] + a)
			okCount = okCount + 1
			print 'OK'
		except:
			brokenCount = brokenCount + 1
			print 'BROKEN'	
		print '*****'
	else:
		print "poop"
		print a

# print out results

print ("OK total count is: %s " % okCount)
print "================================================================="
print ("Broken total count is: %s " % brokenCount)

