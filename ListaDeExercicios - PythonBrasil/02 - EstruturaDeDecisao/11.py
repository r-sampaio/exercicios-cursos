# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
# lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:
    # a. salários até R$ 280,00 (incluindo) : aumento de 20%
    # b. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    # c. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # d. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    # e. salário antes do reajuste;
    # f. percentual de aumento aplicado;
    # g. valor do aumento;
    # h. novo salário, após o aumento.

salario = float(input('Digite o valor do salário: R$'))
porcentagem = salario/100
if salario < 280.00:
    percentual = 20
    aumento = (salario / 100) * percentual
elif salario > 280.00 and salario < 700.00:
    percentual = 15
    aumento = (salario / 100) * percentual
elif salario > 700.00 and salario < 1500.00:
    percentual = 10
    aumento = (salario / 100) * percentual
elif salario > 1500.00:
    percentual = 5
    aumento = (salario / 100) * percentual
print(f'Valor do salário: {salario}')
print(f'O percentual de {percentual} foi aplicado.')
print(f'Com o aumento de: {aumento}')
print(f'Salario + aumento dando o total de: {(salario + aumento):.2f}')
