n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

if (n1+n2)/2 < 5:
    print('Você foi reprovado!!')

elif (n1+n2)/2 > 5 and (n1+n2)/2 < 7:
    print('Você está de recuperação!!')

elif (n1+n2)/2 > 7 and (n1+n2)/2 < 10:
    print('Você está aprovado!!')

else:
    print('Por favor digite valores verdadeiros!')