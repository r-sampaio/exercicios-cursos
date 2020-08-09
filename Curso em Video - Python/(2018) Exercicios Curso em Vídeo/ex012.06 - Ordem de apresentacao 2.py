from random import shuffle

n1 = input('Primeiro: ')
n2 = input('Segundo: ')
n3 = input('Terceiro: ')
n4 = input('Quarto: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem sera, ')
print(lista)