'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros 
vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e 
imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o 
preço do litro do álcool é R$ 1,90.
'''
combustivel = str(input('Vai abastecer com Álcool ou Gasolina [A/G]: '))
litros = float(input('Digite a quantidade de litros: '))
if combustivel in 'Aa':
    if litros <= 20:
        valor = litros * (1.90 - ((1.90/100) * 3))
        print(f'Você irá pagar {valor:.2f} pelos {litros:.2f} de álcool.')
    elif litros > 20:
        valor = litros * (1.90 - ((1.90/100) * 5))
        print(f'Você irá pagar {valor:.2f} pelos {litros:.2f} de álcool.')
elif combustivel in 'Gg':
    if litros <= 20:
        valor = litros * (2.50 - ((2.50/100) * 4))
        print(f'Você irá pagar {valor:.2f} pelos {litros:.2f} de gasolina.')
    elif litros > 20:
        valor = litros * (2.50 - ((2.50/100) * 6))
        print(f'Você irá pagar {valor:.2f} pelos {litros:.2f} de gasolina.')
