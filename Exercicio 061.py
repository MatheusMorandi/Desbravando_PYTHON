#Exercício Python #061 - Progressão Aritmética v2.0

pt = int(input('Qual o primeiro termo da |P.A|: '))
rz = int(input('Qual a |razão|: '))
cont = 0
reg = 9

print(f'{pt} ==>', end = ' ')

while reg >= 0:

    if reg > 0:

        pt += rz

        print(f'{pt} ==>', end = ' ')

    elif reg == 0:

        print('ACABOU')
        
    reg -= 1    