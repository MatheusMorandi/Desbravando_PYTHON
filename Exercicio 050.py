#Exercício Python #050 - Soma dos pares

np = 0

num = 0

p = []

i = 0

for i in range(0,7):
    num = int(input('Digite um número: '))
    i += 1
    p.append(num)
    if num % 2 == 0:
        np += num
        

print(f'Você inseriu esses números {p} e a soma de todos os números \033[;41mpares\033[m digitados foi {np}')