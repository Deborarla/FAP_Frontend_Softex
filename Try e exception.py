nome=str(input('Digite seu nome completo: '))

ano = 1922
while ano:
	try:
		nas_ano=int(input('Digite seu ano de nascimento com 4 digitos a partir de 1922: '))
		if ano <= nas_ano:
			break
	except Exception as e: 
		print(e)
idade = 2022 - nas_ano
print(nome,'voce tem ', str(idade), 'anos')