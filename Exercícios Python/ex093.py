dados_jogador={}
totgols = []
dados_jogador['Nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados_jogador["Nome"]} jogou? '))
for c in range (0, partidas):
    totgols.append(int(input(f'Quantos gols na partida {c+1}? ')))
dados_jogador['gols'] = totgols[:]  
dados_jogador['total'] = sum(totgols) 
print('-=' * 30)
print(dados_jogador)
print('-=' * 30)
for k, v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados_jogador["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate (dados_jogador['gols']):
    print(f' => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados_jogador["total"]} gols.')
print('-=' * 30)