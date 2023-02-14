#Exercício Python #036 - Aprovando Empréstimo

vc = int(input('Digite o valor da casa: '))

vs = int(input('Digite o valor do seu sálario: '))

va = int(input('Digite em quantos anos você gostaria de quitar seu financiamento: '))

vm = vc/(va*12)

if vm<(0.3*vs):
    print(f'Seu empréstimo foi aceito, a parcela custará: {vm}R$')

else:
    print('Seu empréstimo não foi aceito!')
