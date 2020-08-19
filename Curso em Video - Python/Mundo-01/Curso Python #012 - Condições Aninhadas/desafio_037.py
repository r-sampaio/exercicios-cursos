# Escreva um produto que leia um número inteiro qualquer e peça para o usuário escolher
    # qual será a base de conversão:
    # - 1 para binário
    # - 2 para octal
    # - 3 para hexadecimal

print('''Conversor de base númerica:
- 1 para binário
- 2 para octal
- 3 para hexadecimal\n''')
opcao = int(input('Opção: '))
numero = int(input('Digite um número: '))
if opcao == 1:
    print(f'{numero} em binario {bin(numero)[2:]}.')
elif opcao == 2:
    print(f'{numero} em octal {oct(numero)[2:]}.')
elif opcao == 3:
    print(f'{numero} em hexadecimal {hex(numero)[2:]}.')
else:
    print('Digite um número válido')
