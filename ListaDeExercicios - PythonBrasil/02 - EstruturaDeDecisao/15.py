'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores 
podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
isósceles ou escaleno.
    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
'''

lista = [0, 0, 0]
for i in range(0, 3):
    lista[i] = int(input(f'Digite o {i+1}º lado do triângulo: '))
if lista[0] < lista[1] + lista[2] and lista[1] < lista[0] + lista[2] and lista[2] < lista[0] + lista[1]:
    print('Forma um triângulo ', end='')
    if lista[0] == lista[1] == lista[2]:
        print('equilátero.')
    elif lista[0] != lista[1] != lista[2] != lista[0]:
        print('escaleno.')
    else:
        print('isósceles.')
else:
    print('Não forma um triângulo')
