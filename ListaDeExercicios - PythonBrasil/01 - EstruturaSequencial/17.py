'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta 
é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    * comprar apenas latas de 18 litros;
    * comprar apenas galões de 3,6 litros;
    * misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga 
    e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''

from math import ceil

tamanho = float(input('Digite o tamanho da parede em metros quadrados: '))
tipo = str(input('Lata, galão ou os dois? ')).strip().upper()
if tipo in 'LATA':
    s = tamanho / 6 #calcula a quantidade de litros
    b = 80 / 18 #calcula o preco do litro da lata
    c = s * b 
    v = c / 80 # calcula a quantidade de latas
    h = ceil(v)
    f = h * 80
elif tipo == 'GALAO':
    s = tamanho / 6 #calcula a quantidade de litros
    g = 25 / 3.6 #calcula o preco do litro do galão
    c  = s * g
    v = c / 25 # calcula a quantidade de latas
    f = ceil(v)
elif tipo == 'OS DOIS':
    n = int(tamanho / 18)
    l = tamanho%18
    c = ceil(l / 3.6)
    f = (n * 80) + (c * 25)
print(f'Você irá pagar R${f:.2f} por {n} latas e {c} tinta.')
