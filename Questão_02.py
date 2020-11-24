# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANSÃO
# Lista_4

Ld = int(input('Digite o número de lados do Polígono: ')) #Le quantos lados pede 
Md = float(input('Digite a medida do lado do Polígono: ')) #Le a medida do lado
if Ld == 3:
 	area = Md ** 2 * 3 ** (1/2) / 4 #Calcula a área do triângulo
 	print('Triângulo')
 	print(area)
elif Ld == 4: #condição
 	print('Quadrado')
 	area = Md ** 2
 	print(area)
elif Ld == 5:
 	print('PENTÁGONO')
elif Ld < 3:
 	print('NÃO É UM POLÍGONO')
elif Ld > 5:
 print('POLÍGONO NÃO INDENTIFICADO')