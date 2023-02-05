from random import randint
import time
import operator

valores_dados = {}

print('Valores sorteados:')
time.sleep(1)

valores_dados['jogador1'] = randint(1,6)

valores_dados['jogador2'] = randint(1,6)

valores_dados['jogador3'] = randint(1,6)

valores_dados['jogador4'] = randint(1,6)

#print(valores_dados)

for k, v in valores_dados.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)

print('-=' * 30)

ordenando_ranking = []
print('== RANKING DOS JOGADORES ==')
ordenando_ranking = sorted(valores_dados.items(), key=operator.itemgetter(1), reverse=True)
#print(ordenando_ranking[0][1])

for i, l in enumerate(ordenando_ranking):
    print(f'{i+1}º lugar: {l[0]} com {l[1]}')
    time.sleep(1)
print('-' * 30)
print('Fim da execução!')

