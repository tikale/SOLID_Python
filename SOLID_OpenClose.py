# 2. Open Close Principle            - otwarte-zamknięte
#		Close for modification, open for extencion.
#		Klasa jest zamknięta na modyfikacje gdy nie zmieniamy jej istniejącgo kodu.
#		A otwarta na rozbudowę gdy możemy istniejący kod rozszeżać.
#		Przed czyn nas chroni ta zasada np. dodając nową funkcjonalność do klasy A możemy zapsuć działanie zależnej od niej klasy B.
#		Lepszym rozwiązaniem jest dodanie nowej funkcjonalności do nowej klasy C.
#		Tej zasady nie stosujemy w przypadku naprawy błędów.


# Zasada nie jest spełniona, bo dodanie kolejnej figury np. trójkąt modyfikuje funkcje draw_shape
class Shape:
	def __init__(self, name: str):
		self.name = name
	
	def get_name(self) -> str:
		pass
		
shapes = [
Shape('Kwadrat'),
Shape('Okrag')
]

def draw_shape(shapes: list):
	for shape in shapes:
		if shape.name == 'Kwadrat':
			print('To jest Kwadrat')
		elif shape.name == 'Okrag': 
			print('To jest Okrag')
			
draw_shape(shapes)

# Klasa Shape będzie miała metodę wirtualną shapeOC
# A każdy kształt będzie miał osobną klasę z własną wersją metody shapeOC

# Do kwadratu i okręgu dodamy trójkąt.
class Shape_OC:
	def __init__(self, name: str):
		self.name = name
		
	def get_name(self):
		return self.name
		
	def shapeOC(self):
		pass
		
class Kwadrat(Shape_OC):
	def shapeOC(self):
		return 'Kwadrat'

class Okrag(Shape_OC):
	def shapeOC(self):
		return 'Okrag'

class Trojkat(Shape_OC):
	def shapeOC(self):
		return 'Trojkat'
		
def draw_shapeOC(shapes_names_OC: list):
	for shape_name in shapes_names_OC:
		print(f"To jest {shape_name.shapeOC()}.")

shapes_names_OC = [
Shape_OC('Kwadrat'),
Shape_OC('Okrag'),
Shape_OC('Trojkat')
]

for name in shapes_names_OC:
	print (name.get_name())
	
draw_shapeOC(shapes_names_OC)		