# 5. Dependency Inversion Principle  - Odwrócenie zależnosci.
#		Moduły wysokiego poziomu nie powinny zależeć on modułów niskiego poziomu.
#		Oba powinny polegać na abstrakcjach.
#		Abstrakcje nie powinny zależeć od szczegułów.
#		Szczeguły powinny zeleżeć od abstrakcji. 
#		Moduły wysokiego poziomu mówią nam co program ma robić (logika biznesowa). 
#		Niskiego poziomu w jaki sposób mają to robić.

class Engine:
	def SetEngine(self, x):
	if x == 0:
		print('Stop Engine')
	elif x == 1:
		print('move right')
	elif x == -1:
		print('move left')
	

class EngineControl(Engine):
	def positive(self):
		super().SetEngine(1)
	def negative(self):
		super().SetEngine(-1)
	def Stop(self):
		super().SetEngine(0)
		
class ProbeProgram(EngineControl):
	# glebokosc
	def Probe(self):
			#na dno
			#stop
			#na powierzchnie



Obj1 = PrintVariable()
Obj1.printX(5)

Obj2 = Dzialania()
Obj2.Dodaj(x)

		
