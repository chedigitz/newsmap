# import all modules first

import os
import sys
import csv
import urllib2
import re

def seeder():
	sites = ['The Guardian','New York Times','Washington Post','BBC','ABC','CBS','NBC','Reuters','CNN'] # list of the site names 
	seeds = [] #holding list
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
			
seeds = seeder()

def keycheck():
	keys = []
	with open(str(os.sys.path[0]) + '/Keyword List - Sheet1.csv','r') as keylist:
		keywords = csv.reader(keylist)
		for x in keywords:
			keys.append(x[0])
		keylist.close()
		return keys
		
keys = keycheck()

def scraper(s):
	try:
		site = urllib2.urlopen(s)
		html = site.read()
		links = re.findall('<a href=".*?' + '.' + '</a>',html)
		return links
	except:
		return 'Error loading site:' + s

<<<<<<< HEAD
for x in seeds:
	for y in scraper(x[2]):
		print y
=======
for x in sorted(links):
	print x
>>>>>>> 4d480ee7d54bae489389f0bb30783f801b5fb386
