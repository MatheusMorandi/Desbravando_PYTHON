#Exercício Python #074 - Maior e menor valores em Tupla

from random import randint as rd

op = (f'{rd(0 , 10)}', f'{rd(0 , 10)}', f'{rd(0 , 10)}', f'{rd(0 , 10)}', f'{rd(0 , 10)}') 

mai = int(op[0])

men = int(op[0])

if mai < int(op[1]):

    mai = int(op[1])

if mai > int(op[1]):

    mai = mai

elif mai < int(op[2]):

    mai = int(op[2])

elif mai > int(op[2]):

    mai = mai

elif mai < int(op[3]):

    mai = int(op[3])

elif mai > int(op[3]):

    mai = mai

elif mai < int(op[4]):

    mai = int(op[4])

elif mai > int(op[4]):

    mai = mai

else:

    mai = mai

if men > int(op[1]):

    men = int(op[1])

elif men > int(op[2]):

    men = int(op[2])

elif men > int(op[3]):

    men = int(op[3])

elif men > int(op[4]):

    men = int(op[4])

else:

    men = men

print(f'Os números sorteados foram : {op[0]}, {op[1]}, {op[2]}, {op[3]}, {op[4]}')

print(f'O maior número sorteado foi: {mai}')

print(f'O menor número sorteado foi: {men}')