'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
'''

cont = 3
p = 0
s = 1
c = 0
print(f'{p}, {s}, ', end='')
while c < 500:
    c = p + s
    print(f'{c}', end='')
    p = s
    s = c
    cont += 1
    if c > 500:
        break
    print(', ', end='')
