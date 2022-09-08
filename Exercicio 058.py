#Exercício Python #058 - Jogo da Adivinhação v2.0

from random import choice

cl = 0,1,2,3,4,5,6,7,8,9,10

chp = choice(cl)

print('Pensei em um número entre 0 e 10, será que você é capaz de adivinhar qual foi?')

resp = 1

u = int(input('Digite seu palpite: '))

while u != chp:

    resp += 1

    if u > chp:

        u = int(input('Um pouco à menos.... Tente novamente: '))
        
    else:

        u = int(input('Um pouco à mais.... Tente novamente: '))
    
print(f'Parabéns depois de {resp} tentativas você conseguiu adivinhar o número {chp}!')