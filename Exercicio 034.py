#Exercício Python #034 - Aumentos múltiplos

sal = float(input('Digite o valor do seu salário: '))

if sal <=1250:
    print(f'Seu novo salário será de {sal+(sal*0.15)}')

else:
    print(f'Seu novo salário será de {sal+(sal*0.1)}')