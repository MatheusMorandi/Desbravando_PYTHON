#Python Exercício #041 - Classificando Atletas

age = int(input('Digite o ano que você nasceu: '))

ano = int(input('Digite em que ano estamos: '))

if (ano - age) < 9:
    print('Você está na categoria mirim!!')

elif (ano - age) > 9 and (ano - age) < 14:
    print('Você está na categoria infatil!!')

elif (ano - age) > 14 and (ano - age) < 19:
    print('Você está na categoria junior!!')

elif (ano - age) > 19 and (ano - age) < 25:
    print('Você está na categoria sênior!!')

else:
    print('Você está na categoria master!!')

