#Questão 1

Lados = int(input('Digite o número de lados do Polígono: '))
Medida = float(input('Digite a medida do lado do Polígono: '))
if Lados == 3:
Area = Lados ** 2 * 3 ** (1/2) / 4
print('Triângulo')
print(Area)
elif Lados == 4:
print('Quadrado')
Area = Lados ** 2
print(Area)
elif Lados == 5:
print('Pentágono')



#Questão 2

Lados = int(input('Digite o número de lados do Polígono: '))
Medida = float(input('Digite a medida do lado do Polígono: '))
if Lados == 3:
 Area = Lados ** 2 * 3 ** (1/2) / 4
 print('Triângulo')
 print(Area)
elif Lados == 4:
 print('Quadrado')
 Area = Lados ** 2
 print(Area)
elif Lados == 5:
 print('PENTÁGONO')
elif Lados < 3:
 print('NÃO É UM POLÍGONO')
elif Lados > 5:
 print('POLÍGONO NÃO INDENTIFICADO')



#Questão 3

Primeiro = int(input('Digite o primeiro valor: '))
Segundo = int(input('Digite o segundo valor: '))
Terceiro = int(input('Digite o terceiro valor: '))
if Primeiro != Segundo != Terceiro:
if Primeiro > Segundo and Primeiro > Terceiro:
 print('O maior valor é o primeiro: ', Primeiro)
elif Segundo > Primeiro and Segundo > Terceiro:
 print('O maior valor é o segundo: ', Segundo)
elif Terceiro > Primeiro and Terceiro > Segundo:
 print('O maior valor é o terceiro: ', Terceiro)
else:
print('Não pode digitar valores iguais!')



#Questão 4

Primeiro = input('Digite o valor do primeiro lado do triângulo: ')
Segundo = input('Digite o valor do segundo lado do triângulo: ')
Terceiro = input('Digite o valor do terceiro lado do triângulo: ')
if Primeiro == Segundo == Terceiro:
print('Triângulo Equilátero')
elif Primeiro == Segundo != Terceiro or Primeiro != Segundo == Terceiro
or Primeiro == Terceiro != Segundo:
print('Triângulo Isóceles')
else:
print('Triângulo Escaleno')



#Questão 5

ângulo1 = int (input('Digite o valor do primeiro ângulo: '))
ângulo2 = int (input('Digite o valor do segundo ângulo: '))
ângulo3 = int (input('Digite o valor do terceiro ângulo: '))
if ângulo1 + ângulo2 + ângulo3 == 180:
if ângulo1 == 90 or ângulo2 == 90 or ângulo3 == 90:
 print('Triângulo Retângulo')
elif ângulo1 > 90 or ângulo2 > 90 or ângulo3 > 90:
 print('Triângulo Obtusângulo')
elif ângulo1 < 90 and ângulo2 < 90 and ângulo3 < 90:
 print('Triângulo Acutângulo ')
else:
print('Não é um triângulo')



#Questão 6

x = input ('Digite um número inteiro: ')
x = int(x)
for x in range(0,x+1):
print(x)
Questão 7
número = int(input("Digite um número entre 1 e 4: "))
while (número < 1 or número > 4):
 print('Entrada inválida, digite o número novamente')
 número = int(input("Digite um número entre 1 e 4: "))
 continue;
else:
 print('O número informado é:', número)



#Questão 8

print('Para buscar o maior valor dos números informados, digite 0')
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



#Questão 9

número = int(input('Informe um número entre 1000 e 9999: '))
unidades = str(número)
print('O número informado foi:' ,número)
print('Unidade: {}'
 '\nDezena: {}'
 '\nCentena: {}'
 '\nMilhar: {}'
 .format(unidades[3], unidades[2], unidades[1], unidades[0]))