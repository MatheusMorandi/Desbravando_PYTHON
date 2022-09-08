#Exercício Python #071 - Simulador de Caixa Eletrônico

print('=' * 30)

print(f'{(" Caixa Eletrônico "):=^30}')

print('=' * 30)

sac = int(input('Qual o valor do saque? R$'))

tot = sac 

ced = 100

totc = 0

while True:
    
    if tot >= ced:

        tot -= ced

        totc += 1
    
    else:
        
        if totc > 0:
            print(f'Total de {totc} de cédulas de R$ {ced}')

        if ced == 100:

            ced = 50

        elif ced == 50:

            ced = 20

        elif ced == 20: 

            ced = 10

        elif ced == 10:

            ced = 5

        elif ced == 5:

            ced = 1
        totc = 0

        if tot == 0:

            break

print('=' * 30)

print(f'{" Volte sempre ":=^30}')    

print('=' * 30)