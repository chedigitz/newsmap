# import all modules first

import os
import sys
import csv
import urllib2
import re

bin = []

def seeder():
	sites = ['The Guardian','New York Times','Washington Post','BBC','ABC','CBS','NBC','Reuters','CNN'] # list of the site names 
	seeds = [] #holding list
	try:
		with open(str(os.sys.path[0]) + '/News Map Seed List - Sheet1.csv','r') as seedlist:
			data = csv.reader(seedlist)
			for row in data:
				if 'Site Name' in row or row[0] == '':
					pass
				else:
					if row[0] in sites:				#checks if the site changes
						holder = row[0]
					if holder == row[0]:			#checks if it's the homepage
						row[0] = 'Homepage'
					item = [holder,row[0],row[1]] 	#sets the site name, page, and link
					seeds.append(item) 				#adds the item to the seeds list
			seedlist.close()
			return seeds
	except:
		print 'Seed list .csv not found'
			
seeds = seeder()

def keymaker():
	keys = []
	try:
		with open(str(os.sys.path[0]) + '/Keyword List - Sheet1.csv','r') as keylist:
			keywords = csv.reader(keylist)
			for x in keywords:
				keys.append(x[0])
			keylist.close()
			return keys
	except:
		print 'Keyword .csv file not found'
		
keys = keymaker()

def scraper(s):
	try:
		site = urllib2.urlopen(s)
		html = site.read()
		links = re.findall('<a href=".*?' + '.' + '</a>',html)
		return links
	except:
		return 'Error loading site:' + s

for x in seeds:
	for y in scraper(x[2]):
		for z in keys:
			if z in y:
				if y not in bin:
					print z + ' found in ' + y
					bin.append(y)

"""
test area below
"""

#for x in bin:
#	print x


website = 'http://www.bbc.com/news/'

for x in scraper(website):
	if 'http://' not in x[:16] and '#' not in x[:16]:
		print x + '  !!!!! APPEND SITE !!!!'
	else:
		print x
