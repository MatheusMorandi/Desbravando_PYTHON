#Exercício Python #068 - Jogo do Par ou Ímpar

from random import choice as ch

win = 0

lis = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

while True:

    chp = ch(lis)

    print('##' * 15)

    print('|VAMOS JOGAR PAR OU ÍMPAR|')

    print('##' * 15)

    num = int(input('Digite um valor de 0 a 10: '))

    uch = str(input('Par ou Ímpar? [P/I]: ')).upper()

    if num < 10 and num > 0:
        
        if uch == 'P' or uch == 'PAR':
            
            if (num + chp) % 2 == 0:

                print('-=' * 30)

                print(f'Você escolheu {num} o computador escolheu {chp}. Resultado {num + chp}, ou seja PAR VENCEU!!')

                print('-=' * 30)

                print('O JOGADOR VENCEU. Vamos jogar novamente')

                win += 1             
            
            elif (num + chp) % 2 != 0:

                print('-=' * 30)

                print(f'Você escolheu {num} o computador escolheu {chp}. Resultado {num + chp}, ou seja ÍMPAR VENCEU!!')

                print('-=' * 30)

                print(f'O COMPUTADOR VENCEU. Game Over Boy. Você venceu {win} vezes. ')

                break

        elif uch == 'I' or uch == 'ÍMPAR' or uch == 'IMPAR':

            if (num + chp) % 2 == 0:
            
                print('-=' * 30)

                print(f'Você escolheu {num} o computador escolheu {chp}. Resultado {num + chp}, ou seja PAR VENCEU!!')

                print('-=' * 30)

                print(f'O COMPUTADOR VENCEU. Game Over Boy. Você venceu {win} vezes. ')

                break

            elif (num + chp) % 2 != 0:

                print('-=' * 30)

                print(f'Você escolheu {num} o computador escolheu {chp}. Resultado {num + chp}, ou seja ÍMPAR VENCEU!!')

                print('-=' * 30)

                print('O JOGADOR VENCEU. Vamos jogar novamente')

                win += 1
            
        else:
            uch = str(input('Opção não reconhecida. Por favor digite [P] caso queira jogar como PAR ou [I] caso queira jogar de ÍMPAR: ')).upper()          

    elif num > 10 or num < 0:
        print('Valor não reconhecido. Por favor digite um valor de 0 a 10!')