#Exercício Python #072 - Número por Extenso

ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    
    num = int(input('Digite um número entre 0 e 20: '))

    if num < 0 or num > 20:

        print('Valor não reconhecido. Por favor digite um número entre 0 e 20!')

    else:

        print(f'Você digitou o número {ext[num]}!')

        break