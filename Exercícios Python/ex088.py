from random import randint
import time
lista = list()
jogos_1 = list()
print('-' * 35)
print('     JOGUE NA MEGA SENA     ')
print('-' * 35)

jogos = int(input('Quantos jogos você quer que eu gere? '))
totj = 1
while totj <= jogos:
    cont = 0
    while True:
        gerador = randint(1,60)
        if gerador not in lista:
            lista.append(gerador)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos_1.append(lista[:])
    lista.clear()
    totj += 1
for i, l in enumerate(jogos_1):
    print(f'Jogo: {i+1}: {l}')
    time.sleep(1)
print('*' * 35)
print('           BOA SORTE!         ')
print('*' * 35)

    
