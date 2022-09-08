#Exercício Python #052 - Números primos

n = int(input('Digite um número: '))

c = 0

for i in range(1, n + 1):

    if n % i == 0:

        print(f'\033[34m{i}', end = " ")
        c += 1
    else:

        print(f'\033[31m{i}', end = " ")

print(' ')

if c == 2:

    print(f'O número {n} foi divisível {c} vezes, logo ele \033[34mÉ UM NÚMERO PRIMO!!')

else:
    print(f'O número {n} foi divisível {c} vezes, logo ele \033[31mNÃO É UM NÚMERO PRIMO!!')