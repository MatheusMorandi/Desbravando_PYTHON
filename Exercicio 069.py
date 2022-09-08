#Exercício Python #069 - Análise de dados do grupo

mai = 0

conth = 0

contm = 0

hcv = 0

mcv = 0

totp = 0

while True:

    print('=' * 12)

    print('|CADASTRE UMA PESSOA|')

    print('=' * 12)

    ida = int(input('Idade: '))
    
    sex = str(input('Sexo [F/M]: ')).upper()

    op = str(input('Quer continuar? [S/N]: ')).upper()

    if op == 'S' or op == 'SIM':
        
        totp += 1

        if ida > 18:

            mai += 1

            if sex == 'F' or sex == 'FEMININO':
                
                contm += 1

                if ida < 20:

                    mcv += 1

            if sex == 'M' or sex == 'MASCULINO':

                conth += 1

                if ida < 20:

                    hcv += 1
        
        else:

            if sex == 'F' or sex == 'FEMININO':
                
                contm += 1

                if ida < 20:

                    mcv += 1

            if sex == 'M' or sex == 'MASCULINO':

                conth += 1

                if ida < 20:

                    hcv += 1

    else:

        totp += 1

        if ida > 18:

            mai += 1

            if sex == 'F' or sex == 'FEMININO':
                
                contm += 1

                if ida < 20:

                    mcv += 1

            if sex == 'M' or sex == 'MASCULINO':

                conth += 1

                if ida < 20:

                    hcv += 1
        
        else:

            if sex == 'F' or sex == 'FEMININO':
                
                contm += 1

                if ida < 20:

                    mcv += 1

            if sex == 'M' or sex == 'MASCULINO':

                conth += 1

                if ida < 20:

                    hcv += 1
        
        print(f'''Total de pessoas cadastradas {totp}, pessoas com mais de 18 anos {mai}. 
        Ao todo temos {conth} homens cadastrados, sendo {hcv} com menos de 20 anos.
        E temos {contm} mulheres cadastradas, sendo {mcv} com menos de 20 anos.''')

        break