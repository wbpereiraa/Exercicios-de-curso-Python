dados_jogador={}
totgols = []
time = list()

while True:
    dados_jogador.clear()
    dados_jogador['Nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados_jogador["Nome"]} jogou? '))
    totgols.clear()
    for c in range (0, partidas):
        totgols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    dados_jogador['gols'] = totgols[:]  
    dados_jogador['total'] = sum(totgols)
    time.append(dados_jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Resposta apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in dados_jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostra dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')