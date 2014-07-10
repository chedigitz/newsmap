import urllib2
import re

website = 'http://www.bbc.com/news/'
domslash = website.find('/',7)

def scraper(s):
	try:
		site = urllib2.urlopen(s)
		html = site.read()
		links = re.findall('<a href=".*?' + '.' + '</a>',html)
		return links
	except:
		return 'Error loading site'
	
for x in scraper(website):
	if 'http://' not in x[:16] and '#' not in x[:16]:
		print '*****'
		print x
		check = re.findall('\/.*"',x)
		for y in check:
			print y[:-1]
			print website[:domslash] + y[:-1]
			try:
				site = urllib2.urlopen(website[:domslash] + y[:-1])
				print 'OK'
			except:
				print 'BROKEN'
		print '*****'
	else:
		print x
