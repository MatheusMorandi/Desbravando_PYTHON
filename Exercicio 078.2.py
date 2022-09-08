#Exercício Python #078 - Maior e Menor valores na Lista

l = []

m = 0

mn = 0

for i in range(0,5):

    num = int(input(f'Digite o número da posição {i}: '))

    l.append(num)

m = max(l)

mn = min(l)

print('-=' * 20)

print(f'Você digitou os seguintes valores: {l}')

print(f'O maior valor digitado foi: {max(l)} nas posições', end = ' ')

for i, v in enumerate(l):

    if v == m: 

        print(f'|{i}|', end = ' ')

print()

print(f'O menor valor digitado foi: {min(l)} nas posições', end = ' ')

for i, v in enumerate(l):

    if v == mn: 

        print(f'|{i}|', end = ' ')