#Exercício Python #067 - Tabuada v3.0

while True:

    num = int(input('Deseja ver a tabuada de qual número? '))

    if num >= 0 :

        print('-=' * 15)

        print(f"""A tabuadada de {num} é:
        {num} X 1 = {num * 1}
        {num} X 2 = {num * 2}
        {num} X 3 = {num * 3}
        {num} X 4 = {num * 4}
        {num} X 5 = {num * 5}
        {num} X 6 = {num * 6}
        {num} X 7 = {num * 7}
        {num} X 8 = {num * 8}
        {num} X 9 = {num * 9}
        {num} X 10 = {num * 10}""")

        print('-=' * 15)
    
    else:

        print('=' * 27)

        print('PROGRAMA TABUADA encerrado.')

        print('=' * 27)

        break