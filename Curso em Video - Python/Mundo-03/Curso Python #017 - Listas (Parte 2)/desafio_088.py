# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar 
    # quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando 
    # tudo em uma lista composta.

from random import randint
palpite = []
cont = int(input('Quantos jogos você quer? '))
for c in range(0, cont):
    for i in range(0, 6):
        p = randint(1, 60)
        if p not in palpite:
            palpite.append(p)
    palpite.sort()
    print(f'{c+1}º palpite: {palpite}')
    palpite.clear()
