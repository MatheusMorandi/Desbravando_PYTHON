#Exercício Python #074 - Maior e menor valores em Tupla Outra Maneira de fazer

from random import randint as rd

op = (f'{rd(0 , 10)}', f'{rd(0 , 10)}', f'{rd(0 , 10)}', f'{rd(0 , 10)}', f'{rd(0 , 10)}') 

print(f'Os números sorteados foram : {op[0]}, {op[1]}, {op[2]}, {op[3]}, {op[4]}')

print(f'O maior número sorteado foi: {max(op)}')

print(f'O menor número sorteado foi: {min(op)}')