#Exercício Python #053 - Detector de Palíndromo

f = str(input('Digite um frase: ')).upper()

cut = f.split()

fj = ''.join(cut)

inv = ''

for i in range(len(fj) - 1, - 1, - 1):
    inv += fj[i]

print(f'A frase {fj} ao contrário fica {inv}')

if inv == fj:
    print('Logo essa frase é um palíndromo!')

else:
    print('Logo essa frase não é um palíndromo!')