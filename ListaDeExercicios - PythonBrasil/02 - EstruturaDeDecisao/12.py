'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário 
o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o 
exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valorHora = float(input('Digite o valor da hora trabalhada: '))
horasTrabalhada = float(input('Digite a quantidade de horas trabalhadas: '))
bruto = horasTrabalhada * valorHora
inss = (bruto/100) * 10
fgts = (bruto/100) * 11
ir = 0
sindicato = (bruto/100) * 3
print(f'{"Salário Bruto ":.<25}: R$ {bruto}')
if bruto <= 900.00:
    print(f'{"(-) IR":.<25}: isento')
else:
    ir = (bruto/100)
    if bruto <= 1500.00:
        ir *= 5
        print(f'{"(-) IR (5%)":.<25}: R$ {ir}')
    elif bruto > 1500.00 and bruto <= 2500.00:
        ir *= 10
        print(f'{"(-) IR (10%)":.<25}: R$ {ir}')
    elif bruto > 2500.00:
        ir *= 20
        print(f'{"(-) IR (20%)":.<25}: R$ {ir}')

print(f'{"(-) INSS (5%) ":.<25}: R$ {inss}')
print(f'{"FGTS (11%) ":.<25}: R$ {fgts}')
print(f'{"Total de descontos ":.<25}: R$ {ir+inss}')
print(f'{"Salário Liquido ":.<25}: R$ {bruto-(ir+inss)}')
