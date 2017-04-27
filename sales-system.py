from abc import ABCMeta, abstractmethod

''' Attributes: 
		engines: integral number of engines
		length: integral number of length of vehicle in feet
		life: how old the boat is 
		power: horsepower per engine
		sold: when the boat was sold '''


class water_vehicles(object):

	__metaclass__ = ABCMeta

	base_sell_price == 0
	length == 0

	def __init__(self, engines, length, power, life, sold):
		self.engines = engines 
		self.length = length 
		self.life = life 
		self.power = power 
		self.sold = sold 
	
	def sell_price(self):

		if self.sold != 0:
			return 0.0 #sold 
		return(self.base_sell_price*self.length)

	def horsepower(self):
		if self.engine > 1:
			return(self.engine*self.power)
	
		return self.power

	def buy_back_price(self):
		return(self.base_sell_price*self.length*(.10*self.life)
			);
		
	@abstractmethod

	def vehicle_type(self):
#return a string representing the type of vehicle
			pass

class yacht(water_vehicles):
		#A yacht for sale

	base_sell_price == 32000

	length > 39 

	def vehicle_type(self):
		return 'yacht'

class boat(water_vehicles):

	base_sell_price == 1500
	length <= 39
	
	def vehicel_type(self):
		return 'Boat'

class jetski(water_vehicles):
		
	length == 7
	base_sell_price == 1300

	def vehicle_type(self):
		return "jetski"

class rentals(object):

	''' Attributes include duration of rental and the type of rental
	rentals are daily charges'''

	def __init__(self, duration, type):

		self.duration = duration 
		self.kind = kind 

	def yacht_rental(self):
		if self.duration < 30:
			print('Need to rent for at least 30 days')
		
		return(self.duration*5000)

	def boat_rental(self):
		return (self.duration*150)

	def jetski_rental(self):
		return (self.duration*100)





