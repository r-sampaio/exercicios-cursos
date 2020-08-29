# Crie um programa que vai ler vários números e colocar em uma lista.
    # Depois disso, mostre:
    # A) Quantos números foram digitados.
    # B) A lista de valores, ordenada de forma decrescente.
    # C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores.')
print(f'Na ordem decrescente fica dessa forma {lista}')
for pos, i in enumerate(lista):
    if 5 == i:
        print(f'O número 5 foi digitado e esta na posição {pos}')
    elif 5 not in lista:
        print(f'O número 5 não foi digitado')
