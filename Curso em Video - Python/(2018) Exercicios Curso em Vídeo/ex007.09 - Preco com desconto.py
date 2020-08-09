p = float(input('Digite o valor do produto: '))
print('Na promocao de hoje, este produto vai ter 5% de desconto e vai fica por {:.2f} reais.'.format((p/100)*95))
print('o desconto sera de R${}'.format(p*5/100))
print('Novo preco sera {}'.format(p-(p*5/100)))