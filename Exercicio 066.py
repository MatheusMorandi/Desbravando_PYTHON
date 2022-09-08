#Exercício Python #066 - Vários números com flag

cont = 0

som = 0

while True:

    num = int(input('Digite um valor ou se quiser parar digite [999]: '))

    cont += 1

    som += num

    if num == 999:
        print(f'Você digitou {cont - 1} números e a soma deles é {som - 999}')

        break