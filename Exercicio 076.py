#Exercício Python #076 - Lista de Preços com Tupla

lp = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-=' * 20)

print(f'{("Lista de Preços"):^40}')

print('-=' * 20)

for i in range(0, len(lp)):

    if i % 2 == 0:

        print(f'{(lp[i] ):=<30}', end =' ')

    else:
        print(f'R${(lp[i]):>7.2f}')

print('-=' * 20)