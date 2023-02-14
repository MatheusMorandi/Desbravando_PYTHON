#Exercício Python #013 - Reajuste Salarial

s = float(input("Qual o valor do seu sálario? "))
a = int(input("Quantos porcento foi seu aumento? "))

sa = s*(a/100)

ns = s + sa

print(f"Seu novo sálario será de {ns}R$")