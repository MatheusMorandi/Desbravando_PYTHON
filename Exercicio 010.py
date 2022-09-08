v = float(input("Quantos reais(R$) você tem em sua carteira? "))

d = v/4.7

if d<=15:
    print(f"Que pena amigo parece que você só conseguiria comprar {d:.3f} doláres")

else:
    print(f"Caraca amigão você está com metade do PIB brasileiro em suas mãos, ou seja tu tem {d:.3f} doláres!!")