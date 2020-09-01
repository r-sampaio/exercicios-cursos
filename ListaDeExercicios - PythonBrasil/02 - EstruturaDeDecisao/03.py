# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Digite o sexo [M/F]: '))
if sexo in 'Ff':
    sexo = 'Feminino'
elif sexo in 'Mm':
    sexo = 'Masculino'
else:
    sexo = 'Sexo Inválido'
print(sexo)
