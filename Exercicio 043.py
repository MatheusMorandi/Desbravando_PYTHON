#Exercício Python #043 - Índice de Massa Corporal

m = float(input('Digite seu peso em (Kg): '))

h = float(input('Digite sua altura em (m):'))

imc = m / h**2

if imc <= 18.5:
    print('Você está abaixo do peso!!')

elif imc > 18.5 and imc <= 25:
    print('Você está no peso ideal!!')

elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso!!')

elif imc > 30 and imc <= 40:
    print('Você está com obesidade!!')

else:
    print('Você está com obesidade mórbida!!') 