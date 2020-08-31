# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
    # utilizando as seguintes fórmulas:
    # Para homens: (72.7*h) - 58
    # Para mulheres: (62.1*h) - 44.7

sexo = str(input('Digite sue sexo [M/F]: ')).strip()[0]
if sexo in 'Mm':
    altura = float(input('Digite sua altura: '))
    result = (72.7*altura) - 58
elif sexo in 'Ff':
    altura = float(input('Digite sua altura: '))
    result = (62.1*altura) - 44.7
print(f'Seu peso ideal é {result:.2f}kg.')
