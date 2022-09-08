

pt = int(input('Digite o primeiro termo da sua P.A: '))

rz = int(input('Digite a razão da sua P.A: '))

n = [pt]

pa = 0

for i in range (0,9):

    pa = pt + rz

    n.append(pa)

    pt = pa

print(f'Os 10 primeiros termos dessa P.A são : {n}')