#Exercício Python #081 - Extraindo dados de uma Lista

ls = []

cont = 0

nc = bool

num = int(input('Digite um número: '))

ch = str(input('Deseja continuar? [S/N] ').upper())

ls.append(num)

cont += 1

if num == 5:

    nc = True

if ch in ['SIM','S','SIN','SI']:

    while True:

        num = int(input('Digite um número: '))

        ch = str(input('Deseja continuar? [S/N] ').upper())

        ls.append(num)

        cont += 1

        if num == 5:

            nc = True

        if ch in ['SIM','S','SIN','SI']:

            continue

        else:

            ls.sort()

            ls.reverse()

            if nc == True:

                print()

                print(f'Você digitou {cont} elementos\nOs valores em ordem decrescente {ls}\nO valor 5 está presente na lista!')

                print()

            elif nc == False:

                print()

                print(f'Você digitou {cont} elementos\nOs valores em ordem decrescente {ls}\nO valor 5 não está presente na lista!')

                print()
            
            break