# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
    # na ordem de colocação. Depois mostre:
    # a) Os 5 primeiros times.
    # b) Os últimos 4 colocados.
    # c) Times em ordem alfabética.
    # d) Em que posição está o time da Chapecoense.

times = ('Internacional', 'Vasco', 'São', 'Paulo', 'Atlético-MG', 'Palmeiras', 'Santos', 'Fluminense',
          'Bahia', 'Grêmio', 'Athletico-PR', 'Botafogo', 'Corinthians', 'Bragantino', 'Fortaleza',
           'Flamengo', 'Goiás', 'Atlético-GO', 'Sport', 'Ceará', 'Coritiba',)

print(times[:6])
print(times[-4:])
print(sorted(times))
print(times.index('Palmeiras')+1)
