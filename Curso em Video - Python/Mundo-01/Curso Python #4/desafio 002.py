from funcoes import limpa, title, result

limpa()
title()
dia = input('Em que dia você nasceu? ')
limpa()
title()
mes = input('Em que mês você nasceu? ')
limpa()
title()
ano = input('Em que ano você nasceu? ')
limpa()
result()
print('Você nasceu em {}/{}/{}.\n'.format(dia, mes, ano))
