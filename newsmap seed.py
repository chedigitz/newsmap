# import all modules first

import os
import sys
import csv
import urllib2

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
	site = urllib2.urlopen(s)
	html = site.read()
	start, end = 0,0
	links = []
	while start != -1:
		start = html.find('a href="',end) 				 #finds start of '<a href="' tags
		end = html.find('">', start + 8)				 #finds end of '<a href="' tag
		ltexts = html.find('>',end) 					 #finds start of link text
		ltexte = html.find('</a>',end)					 #finds start of '</a>' tags
		linktext = str(html[ltexts + 1:ltexte]).replace('<br>',' ').replace('<br/>',' ').replace('&lsquo;',"'").replace('&rsquo;',"'")
		links.append([linktext,html[start + 8:end]])	 #adds links to links list
		start = html.find('a href="', end + 1)	
	return links
	
links = scraper('http://www.washingtonpost.com/')

for x in sorted(links):
	print x
