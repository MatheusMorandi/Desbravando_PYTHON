#Exercício Python #054 - Grupo da Maioridade

from datetime import date

ano = date.today().year
mi = 0
mai = 0

for i in range(1,8):
    idade = int(input(f'Em que ano a {i}ª pessoa nasceu: '))
    if (ano - idade) >= 18:
        mai += 1
    else:
        mi += 1

print(f'Ao todo temos {mai} maiores de idade e {mi} menores de idade!')