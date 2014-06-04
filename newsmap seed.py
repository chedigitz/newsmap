# import all modules first

import os
import sys
import csv

# set standard variables

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
			
#for x in seeds:
#	print x