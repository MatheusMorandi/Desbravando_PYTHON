#Exercício Python #017 - Catetos e Hipotenusa

import math
co = float(input("Digite o comprimento do cateto oposto do seu triângulo: "))

ca = float(input("Digite o comprimento do cateto adjacente do seu triângulo: "))

hp = math.sqrt(co**2 + ca**2)

print(f"O valor da hipotenusa do seu triângulo é igual a {hp}!!")