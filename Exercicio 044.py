#Exercício Python #044 - Gerenciador de Pagamentos

p = float(input('Digite o preço do seu produto: '))

qp = 0

c = int(input('''Selecione o meio de pagamento: 
[1] À vista no cheque ou dinheiro (10%) de desconto;
[2] À vista no cartão (5%) de desconto;
[3] Em até 2x no cartão s/ juros;
[4] Em 3x ou mais no cartão (20%) de juros;
'''))

if c == 1:
    print(f'Você irá pagar {p * 0.9} pelo produto')

elif c == 2:
    print(f'Você irá pagar {p * 0.95} pelo produto')

elif c == 3:
    print(f'Você irá pagar {p / 2} por parcela')

elif c == 4:
    qp = int(input('Em quantas parcelar você irá pagar? '))
    print(f'Você irá pagar {p * 1.2} em {qp} parcelas sendo o preço por parcela {(p * 1.2) / qp}')

else:
    print('Opção não encontrada')

