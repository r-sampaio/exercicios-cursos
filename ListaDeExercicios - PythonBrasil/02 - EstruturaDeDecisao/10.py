# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou 
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
# ou "Valor Inválido!", conforme o caso.

print(' M - Matutino')
print(' V - Vespertino')
print(' N - Noturno')
turno = str(input('Qual o turno que você estuda: '))
if turno in 'Mm':
    mensagem = 'Bom Dia!'
elif turno in 'Vv':
    mensagem = 'Boa Tarde!'
elif turno in 'Nn':
    mensagem = 'Boa Noite!'
else:
    mensagem = 'Valor Inválido!'
print(mensagem)
