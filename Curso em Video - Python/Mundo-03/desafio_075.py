# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    # A) Quantas vezes apareceu o valor 9.
    # B) Em que posição foi digitado o primeiro valor 3.
    # C) Quais foram os números pares. 

num = int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: '))

print(f'Os numeros digitados foram,', end=' ')
for r in num:
    print(r, end=' ')
print(f'\nO numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 aparece na posição {num.index(3)+1}')
else:
    print('Não foi digitado o numero 3.')
print(f'Os numeros pares digitados foram', end=' ')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')
