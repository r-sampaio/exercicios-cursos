# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
    # Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
    # fechados na ordem correta.

p = 0
lista = []
lista.append(str(input('Digite a expressão: ')))
for i in lista:
    if i == '(' or i == ')':
        p += 1
if p % 2 == 0:
    print('A expressão esta correta.')
else:
    print('A expressão não esta correta.')
