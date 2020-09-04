'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
como "Inocente".
'''

r = 0
print('Responda com sim ou não [S/N]:')
p1 = str(input('Telefonou para a vítima? ')).upper().strip()[0]
if p1 == 'S':
    r += 1
p2 = str(input('Esteve no local do crime? ')).upper().strip()[0]
if p2 == 'S':
    r += 1
p3 = str(input('Mora perto da vítima? ')).upper().strip()[0]
if p3 == 'S':
    r += 1
p4 = str(input('Devia para a vítima? ')).upper().strip()[0]
if p4 == 'S':
    r += 1
p5 = str(input('Já trabalhou com a vítima? ')).upper().strip()[0]
if p5 == 'S':
    r += 1
if r == 2:
    print('Suspeita')
elif 3 <= r <= 4:
    print('Cúmplice')
elif r == 5:
    print('Assassino')
else:
    print('Inocente')
