#variaveis
nome=str( input('Digite o nome do aluno: ') )
nota1=float(input('Digite a primeira nota:'))
nota2=float(input('Digite a segunda nota:'))
falta=int(input('Digite o total de faltas:'))
media=((nota1 + nota2)/2)

#Operadores logicos
if media<7 or falta > 3:
    print(nome, ',voce está reprovado!')
else:
    print(nome, ',voce está aprovado!!')
