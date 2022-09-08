#Exercício Python #065 - Maior e Menor valores

cont = 1

tot = 0

mai = 0

men = 0

num = int(input('Digite um número: '))

men = num

mai = num

tot += num

op = str(input('Deseja continuar? [S/N]: ')).upper()

while op != 'N':

    if op == 'S':

        num = int(input('Digite um número: '))

        if mai > num:
        
            mai = mai
        
        elif mai < num:

            mai = num
        
        elif men > num:
            
            men = num

        op = str(input('Deseja continuar? [S/N]: ')).upper()

        cont += 1

        tot += num

    else:

        op = str(input('Opção não reconhecida. Digite (S) para continuar ou (N) para parar: ')).upper()

print(f'Você digitou {cont} números e a média deles é {tot / cont}\nO maior número foi {mai} e o menor número foi {men}!')