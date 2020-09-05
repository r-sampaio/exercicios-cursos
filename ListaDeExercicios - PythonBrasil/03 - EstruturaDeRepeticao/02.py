# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual 
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = str(input('Digite o nome de usuário: '))
    senha = str(input('Digite a senha: '))
    if usuario != senha:
        break
    else:
        print('ERRO, tente novamente')
print('Parabéns! Seu cadastro foi realizado com sucesso')
print(f'Usuário: {usuario}')
print(f'Senha: {senha}')
