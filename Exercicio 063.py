#Exercício Python #063 - Sequência de Fibonacci v1.0

pt = 0
st = 1
nt = 0

print("-=-=" * 10)

nv = int(input('Quantos termos você quer exibir? '))

print(f'{pt} --> {st} --> ', end = ' ')

while (nv - 2) > 0:

    nt = pt + st

    print(f'{nt} --> ', end = ' ')

    pt = st

    st = nt

    nv -= 1

print('FIM')