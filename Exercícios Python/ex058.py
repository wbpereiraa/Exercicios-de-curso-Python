from random import randint
computador = randint(0, 10) # faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez!')
        elif jogador > computador:
            print('Menos...Tente mais uma vez!')
print('Acertou com {} tentativas! Parabéns!'.format(palpites))
