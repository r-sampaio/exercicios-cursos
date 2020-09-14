# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), 
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

# def leiaDinheiro(msg):
#     valido = False
#     while not valido:
#         entrada = str(input(msg)).replace(',', '.').strip()
#         if entrada.isalpha() or entrada == '': # or entrada.strip() == '':
#             print(f'\033[0;31mERRO: \"{entrada}\" é um preco invalido!\033[m')
#         else:
#             valido = True
#             return float(entrada)


# def leiaInt(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('\033[0;31mErro ! digite um número inteiro válido.\033[m')
#         if ok:
#             break
#     return valor