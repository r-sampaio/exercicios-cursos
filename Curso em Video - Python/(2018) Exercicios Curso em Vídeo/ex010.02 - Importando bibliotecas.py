import math
num = int(input('Digite um Numero: '))
raiz = math.sqrt(num)
print('A raiz de {} eh igual a {:.2f}'.format(num, raiz))
print('a raiz de {} eh igual a {}'.format(num, math.trunc(raiz)))
print('a raiz de {} eh igual a {}'.format(num, math.ceil(raiz)))
print('a raiz de {} eh igual a {}'.format(num, math.floor(raiz)))
