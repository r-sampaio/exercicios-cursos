# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera 
# verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

cont = soma = 0
while True:
    idade = int(input('Digite sua idade: '))
    soma += idade
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
total = soma / cont
if total >= 0 and total <= 25:
    turma = 'jovem'
elif total >= 26 and total <= 60:
    turma = 'adulta'
elif total > 60:
    turma = 'idosa'
print(f'Turma {turma}, com media de idade de {total}')
