

print("-" *20)

c = input("Digite algo: ")


print(f"O que você digitou pertence ao tipo primitivo{type(c)}")

print(f"O que você digitou é numérico? {c.isnumeric()}")

print(f"O que você digitou é alfabético? {c.isalpha()}")

print(f"O que você digitou é alfanúmerico? {c.isalnum()}")

print(f"O que você digitou está em minúsculo? {c.islower()}")

print(f"O que você digitou está em maiúsculo? {c.isupper()}")