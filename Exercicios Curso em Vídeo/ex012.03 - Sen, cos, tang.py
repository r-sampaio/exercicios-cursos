import math

ag = float(input('Digite o angulo desejado: '))
sen = math.sin(math.radians(ag))
cos = math.cos(math.radians(ag))
tang = math.tan(math.radians(ag))
print('O seno desse angulo eh {:.2f}.'.format(sen))
print('O cosseno desse angulo eh {:.2f}.'.format(cos))
print('A tangente desse angulo eh {:.2f}.'.format(tang))
