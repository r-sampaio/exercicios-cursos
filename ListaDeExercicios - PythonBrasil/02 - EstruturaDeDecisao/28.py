'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo 
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da 
compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

print('''Tipo de carne         Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg''')
while True:
    tipo = str(input('Digite o tipo de carne que deseja: ')).lower().strip()
    if tipo in ['file duplo', 'alcatra', 'picanha']:
        break
while True:
    peso = float(input('Quantos quilos: '))
    if peso >= 0:
        break
while True:
    pagamento = str(input('Vai pagra com o cartão Tabajara: ')).strip()[0]
    if pagamento in 'SsNn':
        break
if tipo == 'file duplo':
    if peso <= 5.0:
        carne = peso * 4.90
    elif peso > 5.0:
        carne = peso * 5.80
elif tipo == 'alcatra':
    if peso <= 5.0:
        carne = peso * 5.90
    elif peso > 5.0:
        carne = peso * 6.80
elif tipo == 'picanha':
    if peso <= 5.0:
        carne = peso * 6.90
    elif peso > 5.0:
        carne = peso * 7.80
if pagamento in 'Ss':
    total = carne - ((carne / 100) * 5)
else:
    total = carne
    
print(f'{" Hipermercado Tabajara ":.^30}')
print(f'\n{"Itens":.<25}', end='')
print(' Valor')
print(f'{(tipo.upper()):.<25}', end='')
print(f' R${total:.2f}')
