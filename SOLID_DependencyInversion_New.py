# 5. Dependency Inversion Principle  - Odwrócenie zależnosci.
#		Moduły wysokiego poziomu nie powinny zależeć on modułów niskiego poziomu.
#		Oba powinny polegać na abstrakcjach.
#		Abstrakcje nie powinny zależeć od szczegułów.
#		Szczeguły powinny zeleżeć od abstrakcji. 
#		Moduły wysokiego poziomu mówią nam co program ma robić (logika biznesowa). 
#		Niskiego poziomu w jaki sposób mają to robić.
class EngineMove(object):
	def SetEngine(self):
		pass
		
class EngineStop(EngineMove):
	def SetEngine(self):
		print('Stop Engine')
		
class EngineMoveUp(EngineMove):
	def SetEngine(self):
		print('move up')
		
class EngineMoveDown(EngineMove):
	def SetEngine(self):
		print('move down')
	

class EngineControl(object):
	def __init__(self, enginemove):
			self._engine = enginemove 	# Engine move is injected

if __name__ == '__main__':
	depth = 10	
	for _ in range (depth):
		EngineControl(EngineMoveDown().SetEngine())
	EngineControl(EngineStop().SetEngine())
	for _ in range (depth):
		EngineControl(EngineMoveUp().SetEngine())	
