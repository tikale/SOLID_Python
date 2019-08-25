# klasa prostokąt ma 3 odpowiedzialności
class Rectangle:
	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height
	
	def draw(self):
		#Rysujemy
		print("\"Rysujemy prostokat\"")
		
	def area(self):
		return self.width * self.height

	def printRE(self):
		print (f"Szerokosc = {self.width}")
		print (f"Wysokosc = {self.height}")
		print (f"Powierzchnia = {self.area()}")
# =========================================================		

# We can split it into two...
class GeometricRectangle:
	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height
		
	def printRE(self):
		print (f"Szerokosc = {self.width}")
		print (f"Wysokosc = {self.height}")
		print (f"Powierzchnia = {self.area()}")

class DrawRectangle:
	def draw(self):
	# Do some drawing
		print("\"Rysujemy prostokat\"")
# ==========================================================	

# apply the Facade pattern
class printRE:
	def __init__(self, width=0, height=0, area=0):
		print (f"Szerokosc = {self.width}")
		print (f"Wysokosc = {self.height}")
		print (f"Powierzchnia = {self.area()}")

class GeometricRectangleFa:
	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height
		self.DR = DrawRectangle()
		printRE(width, height, area())

	def area(self):
		return self.width * self.height

	def DrawRe(self):
		return self.DR.draw()

print("No to zaczynamy:")
print("")
print("klasa Rectangle:")
r1 = Rectangle(2, 3)
r1.printRE()
r1.draw()