#Exercício Python #020 - Sorteando uma ordem na lista

import random

a1 = str(input("Digite o nome do aluno: "))
a2 = str(input("Digite o nome do aluno: "))
a3 = str(input("Digite o nome do aluno: "))
a4 = str(input("Digite o nome do aluno: "))

lista = a1,a2,a3,a4

print(f"A ordem de apresentação será {random.sample(lista, k=4)}")