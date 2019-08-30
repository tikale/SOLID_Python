# 1. Single Responsibility Principle - jedna odpowiedzialność
#        Każda funkcja, klasa lub modół powinien mieć tylko jeden powód do zmiany.
#        Taki kod łatwiej zrozumieć, naprawić i utrzymać. Łatwiej się go testuje.

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

# We can split it into three...
class GeometricRectangle:
	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height
		
class DrawRectangle:
	def draw(self):
	# Do some drawing
		print("\"Rysujemy prostokat\"")
		
class PrintRectangleData:
	def __init__(self, width=0, height=0, area=0):
		self.width = width
		self.height = height
		self.area = area
		print (f"Szerokosc = {self.width}")
		print (f"Wysokosc = {self.height}")
		print (f"Powierzchnia = {self.area}")
# ==========================================================	

# The downside of this solution is that the clients of the this code have to deal
# with few classes.  A common solution to this dilemma is to apply the Facade
# pattern.
class RectangleFacade:
	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height
		self.DR = DrawRectangle()
		self.GR = GeometricRectangle(width, height)

	def area(self):
		return self.GR.area() #self.width * self.height

	def DrawRe(self):
		return self.DR.draw()
		
	def PrintREdata(self):
		PrintRectangleData(self.width, self.height, self.area()) 

# =============================================================

# Run script
print("No to zaczynamy:")
print("")
print("klasa Rectangle:")
r1 = Rectangle(2, 3)
r1.printRE()
r1.draw()
print("")
print("klasa RectangleFacade:")
r2 = RectangleFacade(5,9)
r2.DrawRe()
r2.PrintREdata()