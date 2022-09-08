#Exercício Python #077 - Contando vogais em Tupla

lp = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for i in range (0, len(lp)):

    print(f'Na palavra {lp[i]} temos:', end = ' ')
    
    for j in range (0, len(lp[i])):

        if lp[i][j] in 'A,E,I,O,U':
            
            print(lp[i][j], end =' ')
    print()       