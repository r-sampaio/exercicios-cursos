# Crie um programa que faça o computado jogar jokenpô com você.
    # ✊ - Pedra
    # 🤚 - Papel 
    # ✌ - Tesoura

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
0 - Pedra
1 - Papel 
2 - Tesoura
''')
opcao = int(input('Pedra, papel ou tesoura: '))

if computador == 0:
    print(f'Sua escolha foi {itens[opcao]}, e o computador {itens[computador]}.')
    if opcao == 0:
        print('Empate')
    elif opcao == 1:
        print('Você venceu')
    elif opcao == 2:
        print('Computador venceu')
    else:
        print('Jogada invalida')
elif computador == 1:
    print(f'Sua escolha foi {itens[opcao]}, e o computador {itens[computador]}.')
    if opcao == 0:
        print('Computador venceu')
    elif opcao == 1:
        print('Empate')
    elif opcao == 2:
            print('Você venceu')
    else:
        print('Jogada invalida')
elif computador == 2:
    print(f'Sua escolha foi {itens[opcao]}, e o computador {itens[computador]}.')
    if opcao == 0:
        print('Você venceu')
    elif opcao == 1:
        print('Computador venceu')
    elif opcao == 2:
        print('Empate')
    else:
        print('Jogada invalida')
