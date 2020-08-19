# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    # O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    # Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
    # ou então o empréstimo será negado.

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salario? '))
tempo = float(input('Em quanto tempo quer pagar? '))
parcela = valor / (tempo * 12)
porcentagem = (salario / 100) * 30
if porcentagem >= parcela:
    print(f'Emprestimo aprovado você irá para uma parcela de R${parcela:.2f} por {tempo} anos.')
else:
    print(f'Emprestimo reprovado!')
