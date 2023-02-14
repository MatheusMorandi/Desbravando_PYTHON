#Exercício Python #042 - Analisando Triângulos v2.0

r1 = float(input('Primeiro Segmento: '))

r2 = float(input('Segundo Segmento: '))

r3 = float(input('Terceiro Segmento: '))

if (r1+r2)>r3 and (r2+r3)>r1 and (r3+r1)>r2:
    print('Essas retas podem formar um triângulo!')
    if r1 == r2 == r3:
        print('E é um triângulo equilátero ')
    elif r1 != r2 != r3:
        print('E é um triângulo escaleno ')
    else:
        print('E é um triângulo isósceles ')
else:
    print('Essas retas não podem formar um triângulo!')