#Exercício Python #022 - Analisador de Textos

name = str(input("Digite seu nome completo: "))
cut = name.split()
join = "".join(cut)
print(f"Seu nome em letras maiúsculas seria: {name.upper()}")
print(f"Seu nome em letras minúsculas seria: {name.lower()}")
print(f"Seu nome tem {len(join)} caracteres ao total!")
print(f"Seu primeiro nome tem {len(cut[0])} caracteres!")