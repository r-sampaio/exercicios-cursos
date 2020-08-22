# Crie um programa que mostre na tela todos os números pares que estão no intevalo entre 1 e 50.

from time import sleep
for i in range(1, 50):
    if i % 2 == 0:
        print(i)
        sleep(1)
print('FIM')