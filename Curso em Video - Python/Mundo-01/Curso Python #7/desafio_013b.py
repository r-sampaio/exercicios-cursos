'''
Faça um algoritmo que leia o valor de um produto e mostra o preço dele parcelado e a vista.
'''
from funcoes import limpa, title, result

limpa()
title()
produto = float(input('Qual o valor do produto? '))
parcela = str(input('Vai parcelar [S/N]? '))
limpa()
if parcela == 'S':
    pagamento = str(input('Qual o modo de pagamentos boleto ou cartão [B/C]? '))
    if pagamento == 'B':
        desconto = float(input('Qual o desconto pagando no boleto? '))
        print(f'O seu produto vai receber um desconto de {desconto}%, e passará para o valor de {((produto-((produto/desconto/100)))):.2f} \n')
    elif pagamento == 'C':
        taxa = float(input('Qual a taxa de parcelamento? '))
        print(f'O seu produto vai receber um almento de {taxa}%, e passará para o valor de {((produto+((produto/100)*taxa))):.2f} devido a taxa de parcelamento.\n')
    else:
        print('Digite uma opção valida.')
else:
    aVista = float(input('Qual o desconto pagando a vista? '))
    print('Com o desconto de pagamento a vista de {} ')
