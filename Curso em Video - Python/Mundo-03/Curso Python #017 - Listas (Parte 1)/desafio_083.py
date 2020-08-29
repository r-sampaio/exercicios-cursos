# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
    # Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
    # fechados na ordem correta.

p = 0
lista = []
expr = (str(input('Digite a expressão: ')))
for i in expr:
    if i == '(' or i == ')':
        p += 1
if p % 2 == 0:
    print('A expressão esta correta.')
else:
    print('A expressão não esta correta.')


'''
p = 0
lista = []
r = []
expr = (str(input('Digite a expressão: ')))
for i in expr:
    if i == '(':
        r.append('(')
    elif i == ')':
        if len(r) > 0:
            r.pop()
        else:
            r.append(')')
            break
if len(r) == 0:
    print('A expressão esta correta.')
else:
    print('A expressão não esta correta.')
'''
