# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANDÃO
# Lista_4

Primeiro = int(input('Digite o primeiro valor: '))
Segundo = int(input('Digite o segundo valor: '))
Terceiro = int(input('Digite o terceiro valor: '))
if Primeiro != Segundo != Terceiro: #Ve se os lados são iguais
if Primeiro > Segundo and Primeiro > Terceiro:
 	print('Valor maior é o primeiro: ', Primeiro)
elif Segundo > Primeiro and Segundo > Terceiro:
 	print('Valor maior é o segundo: ', Segundo)
elif Terceiro > Primeiro and Terceiro > Segundo:
 	print('Valor maior é o terceiro: ', Terceiro)
else:
	print('Não pode digite valores iguais')