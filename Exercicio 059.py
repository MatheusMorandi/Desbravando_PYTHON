#Exercício Python #059 - Criando um Menu de Opções

op = 0

n1 = int(input('Digite um valor: '))

n2 = int(input('Digite outro valor: '))

while op != 5:

    print('#' * 30)

    op = int(input('''O que você quer fazer com os dois números?
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
    >>>>>>>> Escolha uma opção: '''))
    
    if op == 1: 

        print(f'A soma entre os dois números é igual a {n1 + n2}')
    
    elif op == 2:

        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}') 
       
    elif op == 3:

        if n1 > n2:

            print(f'O maior número entre {n1} e {n2} é {n1}')
                
        else:

            print(f'O maior número entre {n1} e {n2} é {n2}')
           
    elif op == 4:

        n1 = int(input('Digite um número: '))

        n2 = int(input('Digite um outro número: '))
    
    elif op == 5:

        print('Desligando....')

    else:
        
        print('Opção não reconhecida tente novamente')

print('Programa encerrado!')