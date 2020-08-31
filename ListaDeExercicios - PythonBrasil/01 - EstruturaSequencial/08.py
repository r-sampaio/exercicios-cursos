# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valor = float(input('Digite quanto você quer ganhar por horas trabalhadas: R$'))
horas = float(input('Digite quantas horas você trabalhou esse mês: '))
toral = valor * horas
print(f'Você receberá o valor de R${toral} por seu trabalho.')
