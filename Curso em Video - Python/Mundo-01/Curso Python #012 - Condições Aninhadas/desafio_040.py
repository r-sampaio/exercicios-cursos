# Crie um programa que leia duas notas de um aluno e calcule sua média,
    # mostrando uma mensagem no final, de acordo com a média atingida:
    # - Média abaixo de 5.0: REPORVADO
    # - Média entre 5.0 e 6.9: RECUPERAÇÃO
    # - Média 7.0 ou superior: APROVADO

av1 = float(input('Digite a nota da AV1: '))
av2 = float(input('Digite a nota da AV2: '))
media = (av1 + av2) / 2
if media < 5.00:
    print(f'Você ficou com media {media:.2f} e foi REPROVADO.')
elif media >= 5.00 and media <= 6.90:
    print(f'Você esta em RECUPERAÇÃO sua media foi {media:.2f}.')
elif media >= 7.00:
    print(f'Você esta APROVADO, sua media foi {media:.2f}.')
