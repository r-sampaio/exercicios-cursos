# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

while True:
    p = str(input('Todos os lados do quadrado tem o mesmo tamanho? '))
    if p in 'Ss':
        a = int(input('Quanto mede um lado do quadrado? '))
        m = str(input('Unidade de medida: ')).strip()
        r = pow(a, 2)
        print(f'A área do quadrado mede {r:.2f} {m}² e seu dobro equi a {(r*2):.2f} {m}²')
        break
    elif p in 'Nn':
        print('Não é um quadrado.')
        break
