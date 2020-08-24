# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 
    # preço normal e condição de pagamento:
    # - À vista dinheiro / cheque: 10% de desconto
    # - À vista no cartão: 5% de desconto
    # - Em até 2x no cartão: preço normal
    # - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do produto: '))
print('''
1 - À vista dinheiro / cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão
''')
formaPagamento = int(input('Digite a foma de pagamento: '))
if formaPagamento == 1:
    preco = preco - ((preco/100)*10)
elif formaPagamento == 2:
    preco = preco - ((preco/100)*5)
elif formaPagamento == 3:
    preco = preco
elif formaPagamento == 4:
    preco = preco + ((preco/100)*20)
else:
    print('Opção invalida')
print(f'Com essa forma de pagamento eu produto passará a custar {preco}.')
