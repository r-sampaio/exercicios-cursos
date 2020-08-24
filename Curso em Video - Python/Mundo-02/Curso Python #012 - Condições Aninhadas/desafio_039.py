# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    # - Se ele ainda vei se alistar ao seviço militar.
    # - se é a hora de se alistar.
    # - Se já passou do tempo do alistamento.
    # Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
if sexo == 'M':
    nascimento = int(input('Qual o ano de seu nascimento? '))
    ano = date.today().year
    result = ano - nascimento
    difer = result - 18
    dever = ano - difer
    if result < 18:
        print(f'Ainda tem tempo, voce so tem {result} anos')
    elif result == 18:
        print(f'Esta na hora, você completa {result} este ano {ano}')
    elif result > 18:
        print(f'Ja passou da hora, você esta {difer} anos atrasado, deveria ter se alistado em {dever}')
else:
    print(f'Você não precisa se alistar')
