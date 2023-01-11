lista_times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético Paranaense', 
                'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 
                'Coritiba', 'Cuiaba', 'Ceará', 'Goianiense', 'Avaí', 'Juventude')

print('*=' * 100)
print(f'Lista de Times do Brasileirão: {lista_times}')
print('*=' * 100)
print(f'Lista de Times em ordem alfabética: {sorted(lista_times)}')
print('*=' * 100)
print(f'Os 5 primeiros colocados: {lista_times [:5]}')
print('*=' * 100)
print(f' Os 4 últimos são: {lista_times [-4:]}')
print('*=' * 100)

# MINHA RESOLUÇÃO!!!
'''for pos, time in enumerate(lista_times): 
    if time == 'Ceará':
        print(f'O time {time} esta na {pos + 1}ª posição.')'''

# RESOLUÇÃO DO PROFESSOR
print(f'O Ceará está na {lista_times.index("Ceará")+1}ª posição.')





