'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

n = int(input('Quantos termos deseja? '))
cont = 3
p = 0
s = 1
print(f'{p}, {s}, ', end='')
for i in range(cont, n +1):
    c = p + s
    print(f'{c}', end='')
    p = s
    s = c
    cont += 1
    if i == n:
        break
    print(', ', end='')
