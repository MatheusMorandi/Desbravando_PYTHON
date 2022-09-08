#Exercício Python #056 - Analisador completo

idade = 0

h = ''

hmv = 0

fv = 0

f = 0

for j in range(1,5):

    print(f'----- {j}ª PESSOA -----')

    n = str(input('Nome: '))

    i = int(input('Idade: '))

    s = str(input('Sexo M/F: ')).upper()

    if s == 'M':

        idade += i

        if hmv < i:

            hmv = i

            h = n

    elif s == 'F':

        idade += i

        f += 1

        if i < 20:

            fv += 1
    else:
        print('Opção não reconhecida!')

print(f'A média de idade do grupo é de {idade / 4}!')

print(f'O homem mais velho possui {hmv} anos e se chama {h}!')

if fv > 0:

    print(f'O total de mulheres foi de {f} e temos {fv} mulheres com menos de vinte anos!')

else:

    print(f'O total de mulheres foi de {f} não temos nenhuma mulher com menos de vinte anos!')
    