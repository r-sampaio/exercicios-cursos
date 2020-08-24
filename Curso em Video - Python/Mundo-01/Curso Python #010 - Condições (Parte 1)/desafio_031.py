# Desenvolva um programa que pergunte a distância de uma viagem em Km.
    #  * Calcule o preço da passagem, cobrando:
    #  * R$0,50 por Km para viagens de até 200Km.
    #  * R$0,45 para viagens mais longas.

distancia = int(input('Digite a distancia da viagen: '))
if distancia <= 200:
    print(f'Você irá pagar R${(distancia*0.50):.2f} pela distancia de {distancia} da viagem.')
else:
    print(f'Você irá pagar R${(distancia*0.45):.2f} pela distancia de {distancia} da viagem.')
