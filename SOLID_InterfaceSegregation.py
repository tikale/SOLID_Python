# 4. Interface Segregation Principle - Segregacja interfejsów
#		Klient nie powinien polegać na metodach których nie używa.
#		Interfejsy powinny być niewielkie (niewiele metod).
#		Nie powinny mieć więcej niż klasy które obsługują.
#		Powinny mieć jedną odpowiedzialność.

# Jeśli chodzi o pythona to nie wspiera on interfejsów jako takich.
# Interface Segregation Principle możemy tu pokazać jako dziedziczenie po klasie abstrakcyjnej

# Źle
# ===
class Shape_OC:
	def __init__(self):
		pass

	def Draw_Kwadrat(self):
		pass
		
	def Draw_Okrag(self):
		pass
		
	def Draw_Trojkat(self):
		pass
		
		
class Kwadrat(Shape_OC):
	def Draw_Kwadrat(self):
		print ('Kwadrat')

class Okrag(Shape_OC):
	def Draw_Okrag(self):
		print ('Okrag')

class Trojkat(Shape_OC):
	def Draw_Trojkat(self):
		print ('Trojkat')
		
Kwadrat_A = Kwadrat()
Okrag_A	= Okrag()
Trojkat_A = Trojkat()

Kwadrat_A.Draw_Kwadrat()
Okrag_A.Draw_Okrag()
Trojkat_A.Draw_Trojkat()

# Dobrze
# ======
class Kwadrat_Interface:
	def __init__(self):
		pass

	def Draw_Kwadrat(self):
		pass
		
class Okrag_Interface:
	def __init__(self):
		pass

	def Draw_Okrag(self):
		pass
		
class Trojkat_Interface:
	def __init__(self):
		pass

	def Draw_Trojkat(self):
		pass		

class Kwadrat_(Kwadrat_Interface):
	def Draw_Kwadrat(self):
		print ('Kwadrat')

class Okrag_(Okrag_Interface):
	def Draw_Okrag(self):
		print ('Okrag')

class Trojkat_(Trojkat_Interface):
	def Draw_Trojkat(self):
		print ('Trojkat')
		
Kwadrat_B = Kwadrat_()
Okrag_B	= Okrag_()
Trojkat_B = Trojkat_()

Kwadrat_B.Draw_Kwadrat()
Okrag_B.Draw_Okrag()
Trojkat_B.Draw_Trojkat()
