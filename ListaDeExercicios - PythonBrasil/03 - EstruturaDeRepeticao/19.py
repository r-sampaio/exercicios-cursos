'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

cont = 0
while True:
    while True:
        numero = int(input('Digite um número: '))
        if 0 <= numero <= 1000:
            if cont == 0:
                maior = numero
                menor = numero
            elif numero > maior:
                maior = numero
            elif numero < menor:
                menor = numero
            cont += 1
            continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
            if continuar in 'Nn':
                break
        elif numero < 0:
            print('Digite um valor acima de 0.')
        elif numero > 1000:
            print('Digite um valor abaixo de 1000.')
soma = maior + menor
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'A soma entre eles é {soma}')
