#Exercício Python #048 - Soma ímpares múltiplos de três

num = 0

soma = 0

for i in range(1,501,2):
    if i % 3 == 0:
        soma += i
        num += 1

print(f'A soma de todos os {num} valores é igual a {soma}!!')
    