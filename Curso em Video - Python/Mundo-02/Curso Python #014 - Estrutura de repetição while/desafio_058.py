# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
    # Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
    # palpites foram necessários para vencer.

from  random import randint

# p = 1
p = 0
c = randint(0, 10)
a = False
while not a:
    print(c)
    u = int(input('Digite um número entre 0 e 10: '))
    if u == c:
        a = True
    elif u < c:
        print('Maior')
        p += 1
    elif u > c:
        print('Menor')
        p += 1
print(f'Acertou em {p+1} tentativas')
# print(f'Acertou em {p} tentativas')
