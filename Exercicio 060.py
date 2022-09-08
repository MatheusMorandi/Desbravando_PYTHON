#Exercício Python #060 - Cálculo do Fatorial

n = int(input('Digite um número para calcularmos seu fatorial: '))
ft = n
r = 1

print(f'{n}! = ', end = ' ')

while ft > 0:

    if ft > 1:

        print(f'{ft} x', end = ' ')

    else:

        print(f'1 = {r} ', end = ' ')

    r = r * ft
    
    ft -= 1
