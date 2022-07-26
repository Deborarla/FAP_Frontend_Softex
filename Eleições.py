from enum import Enum

class urna (Enum):
	candidato_x = 889
	candidato_y = 847
	candidato_z = 515
	brancos = 1
#variaveis
votox = 0
votoy = 0
votoz = 0
votob = 0
cont = 10
#votação
while cont > 0:
	#Tratamento de exceções
	try:
		voto = int(input("Digite o número do seu candidato: "))
		cont -= 1
		conf = str(input("Deseja confirmar seu voto? [S/N]"))
		print('-=' * 20)
                conf.upper()
		confirma = conf.upper()
		#armazenamento de votos
		if confirma == "S":
			if voto == urna.candidato_x.value:
				votox += 1
			elif voto == urna.candidato_y.value:
				votoy += 1
			elif voto == urna.candidato_z.value:
				votoz += 1
			else: 
				votob += 1
		else:
			continue
	except:
		print ("Erro! Tente novamente digitando apenas números")
	continue
#Verificação vencedor
lista_votos = [votox, votoy, votoz]
vencedor = max(lista_votos)
if votox == vencedor:
	vencedor = urna.candidato_x.name
elif votoy == vencedor:
	vencedor = urna.candidato_y.name
elif votoz == vencedor:
	vencedor = urna.candidato_z.name
else:
	vencedor = urna.brancos.name
#Impressão resultado da eleição
print('O vencedor é o ', vencedor)
print(urna.candidato_x.name, 'recebeu ', votox, 'votos!')
print(urna.candidato_y.name, 'recebeu ', votoy, 'votos!')
print(urna.candidato_z.name, 'recebeu ', votoz, 'votos!')
print(urna.brancos.name, 'recebeu ', votob, 'votos!')



