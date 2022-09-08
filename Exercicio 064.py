#Exercício Python #064 - Tratando vários valores v1.0

cont = 0

som = 0

num = int(input('Digite um número [Quando quiser parar coloque 999]: '))

som += num

while num != 999:
    
    num = int(input('Digite um número [Quando quiser parar coloque 999]: '))

    som += num

    cont +=1

print(f'Você digitou {cont} números e a soma deles é {som - 999}!')