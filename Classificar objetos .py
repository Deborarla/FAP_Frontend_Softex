#Objetos materiais
class grill:
	def __init__ (self, tamanho, temperatura, material):
		self.tamanho = tamanho
		self.temperatura = temperatura
		self.material = material
	def ligar (self):
		self.ligado = true
		print('Grill ligado')
	def desligar (self):
		self.desligar = false
		print('Grill desligado')
	def esquentar (self):
		self.esquentar = true
		print('Esquentando')
		
class bolsa:
	def __init__ (self, tamanho, cor, formato):
		self.tamanho = tamanho
		self.cor = cor
		self.formato = formato 
	def aberta (self):
		self.aberta = true
	def fechada (self):
		self.fechada = false
	def cheia (self):
		self.cheia = true
	def vazia (self):
		self.vazia = false
		
#objetos abstratos
class qualidade:
	def __init__(self, honestidade, bondade, comprensivo):
		self.honestidade = honestidade
		self.bondade = bondade
		self.compreensivo = compreensivo
	def compreensivo (self):
		self.compreensivo = true
	def bondade (self):
		self.bondade = true
	def honestidade (self): 
		self.honestidade = true

class sensacao:
	def __init__ (self, sensacao, humana, animal):
		self.sensacao = sensacao
		self.humana = humana
		self.animal = animal
	def fome (self):
		self.fome = true
	def calor (self):
		self.calor = true
	def frio (self):
		self.frio = true