# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
    # Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os 
    # valores únicos digitados, em ordem crescente.

lista = []
while True:
    valor = int(input(f'Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado.')
    elif valor in lista:
        print('Valor duplicado.')
    c = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        break
lista.sort()
print(lista)
