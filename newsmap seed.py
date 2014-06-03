# import all modules first

import csv

# set standard variables

sc = ['The Guardian','New York Times','Washington Post'] #special cases for seed list organizing

# open seed list .csv file

def printout():
	with open('/Users/joereidl/code/newsmap/News Map Seed List - Sheet1.csv','r') as seedlist:
		data = csv.reader(seedlist)
		for row in data: #prints seed list for easy viewing
			if 'Site Name' in row:
				pass
			elif row[0] == '':
				pass
			else:
				startlink = row[1].find('http://')
				slash = row[1].find('/',startlink + 7)
				if row[0].lower() in row[1][:slash]: #checks for site name in url
					print ''
					print ''
					print row[0] #prints site name
					print ''
				elif row[0] == sc[0] or row[0] == sc[1] or row[0] == sc[2]: #checks for special cases
					print ''
					print ''
					print row[0] #prints site name
					print ''
				else:
					print row
printout()