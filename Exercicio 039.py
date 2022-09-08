nasc = int(input('Digite o ano em que você nasceu: '))
ano = int(input('Em que ano estamos? '))

if (ano-nasc)<18:
    print(f'Você ainda não precisa se alistar ainda faltam {18-(ano-nasc)} anos')

elif (ano-nasc)>18:
    print(f'Você já deveria ter se alistado já se passaram {(ano-nasc)-18} anos')

else:
    print('Parabéns já está na hora do seu alistamento')
