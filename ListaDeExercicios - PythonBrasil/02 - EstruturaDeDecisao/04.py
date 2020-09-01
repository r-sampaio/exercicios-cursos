# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra: '))
if letra in 'aeiou':
    letra = 'vogal'
else:
    letra = 'consoante'
print(letra)
