print('Informe as caracteristicas do veiculo e informaremos a categoria adequada')
#variaveis
rodas=int(input('Quantidade de rodas do veiculo:'))
peso=float(input('Peso do veiculo:'))
passageiros=int(input('Capacidade maxima de passageiros:'))
#condicionais
if rodas ==4 and peso<=3500 and passageiros <=8:
	print('Categoria B');
elif rodas >=4 and peso>=3500 and peso<=6000 and passageiros <=8:
	print('Catetoria C');
elif rodas >=4 and passageiros >8 and peso<6000:
	print('Categoria D');
elif rodas >=4 and peso>6000 and passageiros <=8:
	print('Categoria E');
elif rodas<4:
	print('Categoria A');