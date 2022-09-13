#Exercício Python #080 - Lista ordenada sem repetições

ls = []

for i in range(0,5):

    num = int(input('Digite um valor: '))

    if i == 0 or num > ls[-1]:

        ls.append(num)

        print('Valor adicionado ao final da lista!!')

    else:

        pos = 0

        while pos < len(ls):

            if num <= ls[pos]:

                ls.insert(pos, num)

                print(f'Valor adicionado na posição {pos} da lista!!')

                break
                        
            pos += 1

print()
        
print(f'Os valores digitados foram {ls}')

print()