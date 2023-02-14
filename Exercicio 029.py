#Exercício Python #029 - Radar eletrônico

vel = int(input("Digite a velocidade do seu carro: "))

if vel > 80:
    
    print(f"Você foi multado por ter ultrapassado {vel-80}km/h acima do limite de velocidade(80km/h), sua multa será no valor de {(vel-80)*7}R$")

else:
    print("Parabéns você respeitou o limite de velocidade e não foi multado!")

