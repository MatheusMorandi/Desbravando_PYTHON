#Exercício Python #082 - Dividindo valores em várias listas

ls = []

li = []

lp = []

num = int(input("Digite um número: "))

cho = str(input("Deseja continuar? [S/N]").upper())

ls.append(num)

if num % 2 == 0:

    lp.append(num)

else:

    li.append(num)

if cho in ["SIM","S"]:

    while True:

        num = int(input("Digite um número: "))

        cho = str(input("Deseja continuar? [S/N]").upper())

        ls.append(num)

        if num % 2 == 0:

            lp.append(num)

        else:

            li.append(num)

        if cho in ['SIM','S']:

            continue

        else:

            break

print()

print(f'Lista completa|{ls}|\nLista de números PARES |{lp}|\nLista de números ÍMPARES |{li}|')

print()