# Crie um programa que leia dois valores e mostre um menu na tela:
    # [1] Somar
    # [2] Multiplicar
    # [3] Maior
    # [4] Novos números
    # [5] Sair do programa
    # Seu programa deverá realizar a operação solicitada em cada caso.

p1 = int(input('Digite um valor: '))
p2 = int(input('Digite outro valor: '))
c = False
# opcao = 0
# while opcao != 5:
while not c:
    print(' [1] somar')
    print(' [2] multiplicar')
    print(' [3] maior')
    print(' [4] novos números')
    print(' [5] sair do programa')
    o = int(input('Opção: '))
    if o == 1:
        s = p1 + p2
        print(f'A soma de {p1} com {p2} é {s}')
    elif o == 2:
        s = p1 * p2
        print(f'A multiplicação de {p1} com {p2} é {s}')
    elif o == 3:
        if p1 > p2:
            m = p1
        else:
            m = p2
        print(f'Entre {p1} e {p2}, {m} é maior.')
    elif o == 4:
        p1 = int(input('Digite um novo valor: '))
        p2 = int(input('Digite outro novo valor: '))
    elif o == 5:
        print('FIM')
        c = True
    else:
        print('Opção invalida')
