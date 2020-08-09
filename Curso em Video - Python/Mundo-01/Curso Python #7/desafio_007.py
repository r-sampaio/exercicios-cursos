from funcoes import limpa, title, result

limpa()
title()
nota1 = float(input('Digite a primeira nota: '))
limpa()
nota2 = float(input('Digite a segunda nota: '))
limpa()
result()
print(f'A primeira nota foi {nota1}, e a segunda foi {nota2} ficando assim com media {(nota1 + nota2)/2}.\n')
