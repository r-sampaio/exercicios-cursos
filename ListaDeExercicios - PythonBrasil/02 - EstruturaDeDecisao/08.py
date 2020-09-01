# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

produto = 0
for i in range(0, 3):
    temp = int(input(f'Digite o preço do {i+1}º produto: '))
    if i == 0 or produto > temp:
        produto = temp
print(f'O produto mais barato foi o {produto}')
