import time
#classe cronometro
class cronometro:
	#Variavel
	def __init__ (self, segundos, cont):
		self.segundos = segundos
		self.cont = cont
	#metodo
	def tempo ():
		cont = int(input('Digite o tempo em segundos'))
		segundos = 0
		for segundos in range (0, cont):
			print(segundos)
			segundos += 1
			time.sleep(1)
#objeto 1		
contar = cronometro.tempo ()
#cont = 20
print ('Finalizado!')

contador = cronometro.tempo()
#cont = 10
print ('Tempo esgotado')

crono1 = cronometro.tempo ()
#cont = 5