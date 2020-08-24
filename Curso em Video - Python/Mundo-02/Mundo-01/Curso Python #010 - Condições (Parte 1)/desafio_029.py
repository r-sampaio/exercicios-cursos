# Escreva um programa que leia a velocidade de um carro.
    # * se ele ultrapassar 80Km/h, mostre uma mesnsagem dizendo que ele foi multado.
    # * A multa va custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Digite a velocidade do veiculo: '))
if velocidade <= 80:
    print(f'Você estava a {velocidade} dentro do limite.')
else:
    multa = (velocidade - 80) * 7
    print(f'Você estava a {velocidade} é vai ser multado no valor de R${multa}.')
