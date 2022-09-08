nome = str(input("Digite seu nome completo: ")).title()
cut = nome.split()
copy = ".".join(cut)
paste = copy.rsplit(".",1)

print("Prazer em te conhecer!!")
print(f"Seu primeiro nome é {cut[0]}")
print(f"Seu último nome é {paste[1]}")
