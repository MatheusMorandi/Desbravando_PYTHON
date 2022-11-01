#Exercício Python #083 - Validando expressões matemáticas

exp = str(input('Digite uma expressão: '))

ls = []

for par in exp:

    if par == '(':

        ls.append('(')
    
    elif par == ')':

        if len(ls) > 0:

            ls.pop()

        else:

            ls.append(')')

            break

if len(ls) == 0:

    print()

    print('Sua expressão é válida!')

    print()

else:

    print()

    print('Sua expressão não é válida')

    print()