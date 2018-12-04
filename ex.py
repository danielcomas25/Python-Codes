#!/usr/bin/env python3

class Position :
	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon
	def print (self):
		print ("Latitude: %d Longitude: %d \n" % (self.lat,self.lon))

class MetroStation :
	def __init__(self, name, position):
		self.name = name
		self.position = position
	def print (self):
		print ("Metro Station: %s" % (self.name))
		self.position.print()

class City :
	def __init__(self, name, department, position,description):
		self.name = name
		self.department = []
		self.position = position
		self.description = description
	def print(self):
		print ("Data from the city:\nName:%s\t" %s)
	def addDepartment (self, department) :
		self.department.append (department)
	def printDepartment (self,department) :
		print ("Department:\t")

class Department :
	def  __init__(self, name, cities, region,description):
		self.name = name
		self.cities = []
		self.region = region
		self.description = description
	def print (self) :
		print ("Department:%s\tCities:%s\tDescription:%s\t"%(name,country,description)) 	

class Region (object):
	def  __init__(self, name, country,description):
		self.name = name
		self.country = country
		self.description = description
	def print (self) :
		print ("Region:%s\tCountry:%s\tDescription:%s\t"%(name,country,description))


position = Position(8.9,5.8)
metro = MetroStation("Invalides",position)
metro.print();

