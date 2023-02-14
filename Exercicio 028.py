#Exercício Python #028 - Jogo da Adivinhação v.1.0

import random 

lista = 0,1,2,3,4,5
num = random.choice(lista)
trie = int(input("Estou pensando em um número de 0 a 5, tente acertar: "))

if trie == num:
    print("Nossa você acertou, fui derrotado parabéns!!")

else:
    print("HUAHUAUAHUAHUAHU parece que você não é páreo para meu CPU, tente uma próxima vez!!")
