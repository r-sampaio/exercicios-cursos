'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque 
e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 
1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve 
se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, 
uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, 
quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

while True:
    valor = int(input('Digite o valor que deseja sacar: R$'))
    if 10 <= valor <= 600:
        if valor > 100:
            cem = int(valor / 100)
            valor = valor - (cem * 100)
            print(f'{cem} de 100 reais')
        if 50 <= valor < 100:
            cinquenta = int(valor / 50)
            valor = valor - (cinquenta * 50)
            print(f'{cinquenta} de 50 reais')
        if 10 <= valor < 50:
            dez = int(valor / 10)
            valor = valor - (dez * 10)
            print(f'{dez} de 10 reais')
        if 5 <= valor < 10:
            cinco = int(valor / 5)
            valor = valor - (cinco * 5)
            print(f'{cinco} de 5 reais')
        if 1 <= valor < 5:
            um = int(valor / 1)
            valor = valor - (um * 1)
            print(f'{um} de 1 real')
        break
    else:
        if valor < 10:
            print('Valor mínimo 10 reais')
        elif valor > 600:
            print('Valor máximo 600 reais')
