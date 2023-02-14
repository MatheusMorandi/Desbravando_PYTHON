#Exercício Python #011 - Pintando Parede

l = float(input("Qual a largura da sua parede? "))
h = float(input("Qual a altura da sua parede? "))

a = l*h

qt = a/2

print(f"A sua parede mede {a} metros quadrados e serão necessários {qt:.3f} litros de tinta para pinta-lá!")