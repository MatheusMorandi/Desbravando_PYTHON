#Exercício Python #032 - Ano Bissexto

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0:
    print('Você digitou um ano bissexto!!')

else:
    print('Esse não é um ano bissexto!!')