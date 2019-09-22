# 3. Liskov Substitution Principle   - Liskov
#		Jeśli S jest podtypem T, to obiekty T mogą być zastępowane obiektami typu S bez modyfikowania funkcjonalności programu. 
#		np. klasa ptak ma funkcje lataj, pingwin dziedziczy po klasie ptak, ale ponieważ jest nielotem funkcja lataj dla pingwina nie ma sensu.
#		Dlatego wramach zgodności z zasadą Liskov. Pingwin nie może dziedziczyć po klasie ptak.

class Bird:
	def __init__(self):
		pass
		
	def fly(self):
		pass

	def eat(self):
		pass

class Penguin(Bird):  # Pingwin nie lata więc odziedziczona metoda fly nie będzie używana.	 
	pass
	
class Sparrow(Bird):  # Możemy użyć wszystkich funkcji z klasy Bird 
	pass
	
class Animal:
		def __init__(self):
			pass
			
		def eat(self):
			pass
			
class Penguin(Animal):  # Pingwin nie lata więc odziedziczona metoda fly nie będzie używana.	 
		def __init__(self):
			pass
			
		def fly(self):
			pass
	
class Sparrow(Animal):  # Możemy użyć wszystkich funkcji z klasy Bird 
	pass

