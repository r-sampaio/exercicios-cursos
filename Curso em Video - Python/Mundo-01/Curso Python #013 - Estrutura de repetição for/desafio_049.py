# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

def div():
    for l in range(0, 4):
        print('-' * 17, end='')
        print('  ', end='')


numero = int(input('Digite um número: '))
div()
print('')
for i in range(1, 11):
    print(f'| {numero:<2} + {i:<2} = {(numero + i):<3} |  ', end='')
    print(f'| {numero:<2} - {i:<2} = {(numero - i):<3} |  ', end='')
    print(f'| {numero:<2} x {i:<2} = {(numero * i):<3} |  ', end='')
    print(f'| {numero:<2} / {i:<2} = {(numero / i):<3.1f} |')
div()
