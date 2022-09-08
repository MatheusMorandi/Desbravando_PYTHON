p = float(input("Qual o preço do produto desejado? "))
d = int(input("Qual a porcentagem de desconto? "))

pd = p*(d/100)

np = p - pd

print(f"O novo preço do seu produto será de {np}R$")