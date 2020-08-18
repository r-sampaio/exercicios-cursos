# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    # * Para salário superiores a R$1.250,00, calcule um aumento de 10%.
    # * Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salario: '))
if salario >= 1250.00:
    print(f'Você recevera um almento de 10% ficando no valor de R${salario+((salario/100)*10)}.')
else:
    print(f'Você recevera um almento de 15% ficando no valor de R${salario+((salario/100)*15)}.')
