#Exercício Python #055 - Maior e menor da sequência

mai = 0

men = 0

for i in range(1, 6):

    p = float(input(f'Qual o peso da {i}ª pessoa: '))

    men = p

    if mai > p:

        mai = mai
    
    elif mai < p:

        mai = p
    
    elif men < p:
        
        men = p

print(f'O maior peso digitado foi {mai}!\nO menor peso digitado foi {men}')    
