from math import trunc
num = float(input('digite um numero fracionado: '))
print('A parte inteira desse numero eh {}.'.format(trunc(num)))
print('A parte inteira desse numero eh {:.0f}.'.format(num))
print('A parte inteira desse numero eh {}.'.format(int(num)))