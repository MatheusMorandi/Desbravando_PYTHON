#Exercício Python #015 - Aluguel de Carros

d = int(input("Quantos dias você ficou com o carro? "))
km = int(input("Quantos quilometros você andou com o carro? "))

pkm = km * 0.15

pd = d * 60

print(f"Você vai pagar {pd+pkm}R$ pelo carro")
