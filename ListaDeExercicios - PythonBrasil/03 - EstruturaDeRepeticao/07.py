'''
Faça um programa que leia 5 números e informe o maior número.
'''

for i in range(0, 5):
    num = int(input('Digite um numero: '))
    if i == 0 or num > maior:
        maior = num
print(f'O maior numero digitado foi {maior}')
