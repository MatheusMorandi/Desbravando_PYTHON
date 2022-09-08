km = int(input('Quantos kms você andou com o carro? '))

if km <= 200:
    print(f'O preço do seu aluguel é {km*0.5}R$')

else:
    print(f'O preço do seu aluguel é {km*0.45}R$')