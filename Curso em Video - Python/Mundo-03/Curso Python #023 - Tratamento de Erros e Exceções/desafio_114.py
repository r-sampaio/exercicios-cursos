# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

# from urllib import request, error
# # import urllib
# # import urllib.request


# try:
#     #site = urllib.request.urlopen('http://www.pudim.com.br')
#     site = request.urlopen('http://www.pudim.com.br')
# #except urllib.error.URLError:
# except error.URLError:
#     print('\033[31mO site Pudim não está acessível de momento\033[m')
# else:
#     print('\033[32mO site Pudim está acessível\033[m')



# import socket
# host = 'www.pudim.com.br'
# conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conexao.settimeout(.5)
# try:
#     teste = conexao.connect_ex((host, 80))
#     if teste == 0:
#         print('Consegui acessar o site do pudim com sucesso')
# except:
#     conexao.close()
#     print('O site do pudim não está acesssível no momento')
