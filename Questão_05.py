# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANSÃO
# Lista_4

primeiro = int(input('Digite o primeiro valor do triângulo: '))
segundo = int(input('Digite o segundo valor do triângulo: '))
terceiro = int(input('Digite o terceiro valor do triângulo: '))
if primeiro != segundo != terceiro:  #checa as diferenças
if primeiro > segundo and primeiro > terceiro:
	print('O maior valor é o primeiro: ', primeiro)
elif segundo > primeiro and segundo > terceiro:
    print('O maior valor é o segundo: ', segundo)
elif terceiro > primeiro and terceiro > segundo:
    print('O maior valor é o terceiro: ', terceiro)
else:
    print('Não digite valores iguais!')