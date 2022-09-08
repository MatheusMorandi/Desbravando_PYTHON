r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if (r1+r2)>r3 and (r2+r3)>r1 and (r3+r1)>r2:
    print('Essas retas podem formar um triângulo!')

else:
    print('Essas retas não podem formar um triângulo!')