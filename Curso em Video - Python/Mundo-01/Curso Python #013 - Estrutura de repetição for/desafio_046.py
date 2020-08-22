# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
    # indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
from emoji import emojize
for r in range(10, 0, -1):
    print(r)
    sleep(1)
print(emojize('o/ :fireworks:'))
