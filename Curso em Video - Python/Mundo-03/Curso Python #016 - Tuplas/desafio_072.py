# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    # Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
            'dezoito', 'dezenove', 'vinte')

#num = int(input('Digite um numero: '))

#print(numero[num])

while True:
    num = int(input('Digite um numero: '))
    if num >= 0 and num <= 20:
        break
print(numero[num])
