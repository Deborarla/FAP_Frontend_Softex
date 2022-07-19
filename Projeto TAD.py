class Complexo:
	''' Construtor '''
	def __init__ (self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		'''equações'''
	def soma_complexo (self):
		complexo = self.a + self.b + self.c
		print(complexo.real)
		print(complexo.imag)
		return 'Soma numeros complexos' + str(complexo)
	def subtracao_complexo (self):
		complexo = self.a - self.b - self.c
		print(complexo.real)
		print(complexo.imag)
		return 'Subtração numeros complexos' + str(complexo)
	def divisao_complexo (self):
		complexo = self.a / self.b / self.c
		print(complexo.real)
		print(complexo.imag)
		return 'Divisão numeros complexos' + str(complexo)	 
	def multiplicacao_complexo (self):
		complexo = self.a * self.b * self.c
		print(complexo.real)
		print(complexo.imag)
		return 'Multiplicação numeros complexos' + str(complexo)
		
dados = Complexo(2+7j, 3+8j, 1+4j)
print(dados)
s = dados.soma_complexo()
print(s)
sub = dados.subtracao_complexo()
print(sub)
d = dados.divisao_complexo()
print(d)
m = dados.multiplicacao_complexo()
print(m)