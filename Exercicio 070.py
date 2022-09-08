#Exercício Python #069 - Análise de dados do grupo

tot = 0

pmb = ''

pb = 0

cont = 0

print('-=' * 20)

print(f'{(" MORANDI STORE "):-=^40}')

print('-=' * 20)

while True: 

    name = str(input('Nome do produto: ')).title()

    price = float(input('Preço do produto: R$'))

    op = str(input('Deseja continuar? [S/N]: ')).upper()

    tot += price

    if tot == 1:
            
        pb = price

        pmb = name

    else:
        
        if pb > price:
                
            pb = price 

            pmb = name

    if price > 1000:

        cont += 1


    if op == 'N' or op == 'NÃO' or op == 'NAO':

        print('-=' * 20)

        print(f'{("|COMPRAS ENCERRADAS|"):-=^40}')

        print(f'''O total da compra foi {tot:.2f}.
        Temos {cont} produtos custando mais de R$1000,00.
        O produto mais barato foi {pmb} custando R${pb}.''')

        print('-=' * 20)

        break