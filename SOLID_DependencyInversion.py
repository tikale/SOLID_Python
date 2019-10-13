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
			print('move up')
		elif x == -1:
			print('move down')
	

class EngineControl(Engine):
	def positive(self):
		super().SetEngine(1)
	def negative(self):
		super().SetEngine(-1)
	def Stop(self):
		super().SetEngine(0)
		
class ProbeProgram(EngineControl):
	depth = 10
	def Probe(self):
		for _ in range (self.depth):
			super().negative()
		super().Stop()
		for _ in range (self.depth):
			super().positive()



Prob_1 = ProbeProgram()
Prob_1.Probe()		
