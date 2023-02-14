#Exercício Python #018 - Seno, Cosseno e Tangente

import math
n = int(input("Digite um ângulo: "))

sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))

print(f"O seno desse ângulo equivale a {sen:.2f}\nO cosseno equivale a {cos:.2f}\nE a tangente é igual a {tan:.2f}")