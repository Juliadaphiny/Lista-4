# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANSÃO
# Lista_4

y = int(input("Digite um número entre 1 e 4: ")) #pega o número
while (y < 1 or y > 4): #Ve se e 1, 2 , 3 ou 4 se for sai direto caso não seja entra no while 
 print('Entrada inválida, digite o número novamente')
 y = int(input("Digite um número entre 1 e 4: "))
 continue;
else:
 print('O número informado é:', y) #printa o número que digitou entre 1 e 4 
