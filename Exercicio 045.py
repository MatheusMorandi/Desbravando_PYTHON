#Exercício Python #045 - GAME: Pedra Papel e Tesoura

from random import choice

ch = int(input('''
[0] Pedra 
[1] Papel
[2] Tesoura
 '''))

c = [0,1,2]

cc = choice(c)

if ch == 0 and cc == 0:
    print(f'Você escolheu Pedra e eu também escolhi pedra = Empate!!')

elif ch == 0 and cc == 1:
    print(f'Você escolheu Pedra e eu escolhi Papel = Eu venci!!')

elif ch == 0 and cc == 2:
    print(f'Você escolheu Pedra e eu escolhi Tesoura = Você venceu!!')

elif ch == 1 and cc == 0:
    print(f'Você escolheu Papel e eu escolhi Pedra = Você venceu!!')

elif ch == 1 and cc == 1:
    print(f'Você escolheu Papel e eu também escolhi Papel = Empate!!')

elif ch == 1 and cc == 2:
    print(f'Você escolheu Papel e eu escolhi Tesoura = Eu venci!!')

elif ch == 2 and cc == 0:
    print(f'Você escolheu Tesoura e eu escolhi Pedra = Eu venci!!')

elif ch == 2 and cc == 1:
    print(f'Você escolheu Tesoura e eu escolhi Papel = Você venceu!!')

elif ch == 2 and cc == 2:
    print(f'Você escolheu Tesoura e eu também escolhi Tesoura = Empate!!')

else:
    print('Opção não reconhecida')
