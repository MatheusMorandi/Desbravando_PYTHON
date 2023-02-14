#Exercício Python #026 - Primeira e última ocorrência de uma string

frase = str(input("Digite uma frase: ")).upper()
espace = frase.strip()

print(f"A letra 'A' apareceu {espace.count('A')} vezes na sua frase.")
print(f"A primeira letra 'A' se encontra na posição {espace.find('A')+1}.")
print(f"E a última na posição {espace.rfind('A')+1}")