#Exercício Python #052 - Números primos Outra Maneira de Fazer

n = int(input('Digite um número: '))

ld = list()

lf = list()

for i in range(1, n + 1):

    if n % i == 0:

        ld.append(i)

        lf.append(i)

    else:
        lf.append(i)

if len(ld) == 2:

    print(lf)

    print(f'O número {n} foi dividido {len(ld)} vezes, por {ld}, logo ele \033[32mÉ UM NÚMERO PRIMO!!')

else:

    print(lf)

    print(f'O número {n} foi dividido {len(ld)} vezes, por {ld}, logo ele \033[34mNÃO É UM NÚMERO PRIMO!!')