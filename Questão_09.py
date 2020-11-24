# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANSÃO
# Lista_4

print('Digite algum númro, encerre o programa digitando 0')
a = 1
maior = 0
quantidade = 0
while a != 0:
 a = int(input('Valor: '))
 quantidade +=1
if quantidade == 1:
 maior = quantidade = a
else:
 if a > maior:
 maior = a
print(maior)