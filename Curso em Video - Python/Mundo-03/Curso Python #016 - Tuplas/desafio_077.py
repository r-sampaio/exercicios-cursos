# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, 
    # você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('learn', 'forget', 'preachers', 'listened', 'gotta', 
'healing', 'rails', 'going ', 'Thats', 'cannot', 'mentally', )
for i in palavras:
    print(f'\nPara a palavra {i} temos: ', end='')
    for l in i:
        if l.lower() in 'aeiou':
            print(l, end=' ')
