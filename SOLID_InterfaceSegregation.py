# 4. Interface Segregation Principle - Segregacja interfejsów
#		Klient nie powinien polegać na metodach których nie używa.
#		Interfejsy powinny być niewielkie (niewiele metod).
#		Nie powinny mieć więcej niż klasy które obsługują.
#		Powinny mieć jedną odpowiedzialność.

# Jeśli chodzi o pythona to nie wspiera on interfejsów jako takich.
# Interface Segregation Principle możemy tu pokazać jako dziedziczenie po klasie abstrakcyjnej

# Źle
class Shape_OC:
	def __init__(self, name: str):
		self.name = name
		
	def get_name(self):
		return self.name
		
	def Draw_Kwadrat(self):
		pass
		
	def Draw_Okrag(self):
		pass
		
	def Draw_Trojkat(self):
		pass
		
		
class Kwadrat(Shape_OC):
	def Draw_Kwadrat(self):
		return 'Kwadrat'

class Okrag(Shape_OC):
	def Draw_Okrag(self):
		return 'Okrag'

class Trojkat(Shape_OC):
	def Draw_Trojkat(self):
		return 'Trojkat'