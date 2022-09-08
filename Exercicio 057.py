#Exercício Python #057 - Validação de Dados

s = str(input('Digite seu sexo M/F: ')).strip().upper()[0]

while s != 'm' and s != 'M' and s != 'f' and s != 'F':
    s = str(input('Dado inválido. Por favor digite seu sexo M/F: '))

print('Dado computado. Obrigado!')