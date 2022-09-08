#Exercício Python #078 - Maior e Menor valores na Lista

l = []

m = 0

mn = 0

for i in range(0,5):

    num = int(input(f'Digite o número da posição {i}: '))

    l.append(num)

m = max(l)

mn = min(l)

print('-=' * 20)

print(f'Você digitou os seguintes valores: {l}')

print(f'O maior valor digitado foi: {max(l)} nas posições', end = ' ')

if m == l[0]:

    print('0', end = ' ')

    if m == l[1]:

        print('1', end = ' ')

        if m == l[2]:

            print('2', end = ' ')

            if m == l[3]:

                print('3', end = ' ')

                if m == l[4]:

                    print('4', end = ' ')

    elif m == l[2]:

        print('2', end = ' ')

        if m == l[3]:

            print('3', end = ' ')

            if m == l[4]:

                 print('4', end = ' ')

    elif m == l[3]:

        print('3', end = ' ')

        if m == l[4]:

            print('4', end = ' ')

    if m == l[4]:

        print('4', end = ' ')
        
elif m == l[1]:

    print('1', end = ' ')

    if m == l[2]:

        print('2', end = ' ')

        if m == l[3]:

            print('3', end = ' ')

            if m == l[4]:

                print('4', end = ' ')

    elif m == l[3]:

        print('3', end = ' ')

        if m == l[4]:

            print('4', end = ' ')
    
    elif m == l[4]:

        print('4', end = ' ')

elif m == l[2]:

    print('2', end = ' ')

    if m == l[3]:

        print('3', end = ' ')

        if m == l[4]:

            print('4', end = ' ')

    elif m == l[4]:

        print('4', end = ' ')

elif m == l[3]:

    print('3', end = ' ')

    if m == l[4]:

        print('4', end = ' ')       

elif m == l[4]:

    print('4', end = ' ')

print()

print(f'O menor valor digitado foi: {min(l)} nas posições', end = ' ')


if mn == l[0]:

    print('0', end = ' ')

    if mn == l[1]:

        print('1', end = ' ')

        if mn == l[2]:

            print('2', end = ' ')

            if mn == l[3]:

                print('3', end = ' ')

                if mn == l[4]:

                    print('4', end = ' ')

    elif mn == l[2]:

        print('2', end = ' ')

        if mn == l[3]:

            print('3', end = ' ')

            if mn == l[4]:

                 print('4', end = ' ')

    elif mn == l[3]:

        print('3', end = ' ')

        if mn == l[4]:

            print('4', end = ' ')

    if mn == l[4]:

        print('4', end = ' ')

        
elif mn == l[1]:

    print('1', end = ' ')

    if mn == l[2]:

        print('2', end = ' ')

        if mn == l[3]:

            print('3', end = ' ')

            if mn == l[4]:

                print('4', end = ' ')

    elif mn == l[3]:

        print('3', end = ' ')

        if mn == l[4]:

            print('4', end = ' ')
    
    elif mn == l[4]:

        print('4', end = ' ')

elif mn == l[2]:

    print('2', end = ' ')

    if mn == l[3]:

        print('3', end = ' ')

        if mn == l[4]:

            print('4', end = ' ')

    elif mn == l[4]:

        print('4', end = ' ')

elif mn == l[3]:

    print('3', end = ' ')

    if mn == l[4]:

        print('4', end = ' ')       

elif mn == l[4]:

    print('4', end = ' ')