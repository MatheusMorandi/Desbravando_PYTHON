num = int(input('Digite qualquer número inteiro: '))
choice = int(input('''Escolha uma base para conversão
[1] Base Binária
[2] Base Octal
[3] Base Hexadecimal
[4] Exibir em todas as bases acima
'''))

if choice == 1:
    print(f'O número {num} convertido em binário fica {bin(num)[2:]}')

elif choice == 2:
    print(f'O número {num} convertido em octal fica {oct(num)[2:]}')

elif choice == 3:
    print(f'O número {num} convertido em hexadecimal fica {hex(num)[2:]}')

elif choice == 4:
    print(f'O número {num} convertido em binário fica {bin(num)[2:]}, em octal fica {oct(num)[2:]} e em hexadecimal fica {hex(num)[2:]}')

else:
    print('Opção não identificada')