# Faça um programa que calcule o valor total investido por um colecionador 
# em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário 
# deverá informar a quantidade de CDs e o valor para em cada um.

total = media = cont = 0
cds = int(input('Digite o total de CDs: '))
for i in range(cds):
    preco = float(input(f'Qual o valor gasto no {i+1}º CD? '))
    total += preco
    cont += 1
media = total / cont
print(f'Valor total gasto é de: {total:.2f}')
print(f'Valor medio por CD: {media:.2f}')
