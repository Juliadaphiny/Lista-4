# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANSÃO
# Lista_4

ângul_1 = int (input('Digite o valor do primeiro ângulo: '))
ângul_2 = int (input('Digite o valor do segundo ângulo: '))
ângul_3 = int (input('Digite o valor do terceiro ângulo: '))
if ângul_1 + ângul_2 + ângul_3 == 180:
	if ângul_1 == 90 or ângul_2 == 90 or ângul_3 == 90:
 		print('Triângulo Retângulo')
	elif ângul_1 > 90 or ângul_2 > 90 or ângul_3 > 90:
 		print('Triângulo Obtusângulo')
	elif ângul_1 < 90 and ângul_2 < 90 and ângul_3 < 90:
 		print('Triângulo Acutângulo ')
else:
	print('Não é um triângulo')