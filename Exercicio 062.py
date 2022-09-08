#Exercício Python #062 - Super Progressão Aritmética v3.0

pt = int(input('Qual o primeiro termo da |P.A|: '))
rz = int(input('Qual a |razão|: '))
cont = 1
reg = 9

print(f'{pt} ==>', end = ' ')

while reg >= 0:

    if reg > 0:

        pt += rz

        print(f'{pt} ==>', end = ' ')

        cont += 1

    elif reg == 0:

        print('Pausa')
        reg = int(input('Quantos termos vc deseja mostrar a mais? '))

        if reg > 0:
            reg = 1 + reg

        elif reg == 0:
            print(f'Progressão finalizada foram exibidos {cont} termos.')

    reg -= 1    