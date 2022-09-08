#Exercício Python #079 - Valores únicos em uma Lista

ls = []

m = 0

mn = 0

n = int(input('Digite um valor: '))

ls.append(n)

ch = str(input('Deseja continuar? (S/N): ')).upper()

while ch == 'S' or ch == 'SIM':

    n = int(input('Digite um valor: '))

    if n in ls:
        
        print('Você ja inseriu esse valor. Tente outro!!')

        ch = str(input('Deseja continuar? (S/N): ')).upper()

    else:

        ls.append(n)

        ch = str(input('Deseja continuar? (S/N): ')).upper()

ls.sort()

print(f'Você digitou os seguintes valores: {ls}')
