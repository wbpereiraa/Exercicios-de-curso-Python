#MINHA RESOLUÇÃO
'''matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = []
soma3coluna = []
maiorvalor2linha = []
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par.append(matriz[l][c])
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma total dos valores pares digitados é igual a {sum(par)}.')
soma3coluna.append(matriz[0][2])
soma3coluna.append(matriz[1][2])
soma3coluna.append(matriz[2][2])
print(f'A soma dos valores da terceira coluna é {sum(soma3coluna)}.')
maiorvalor2linha.append(matriz[1][0])
maiorvalor2linha.append(matriz[1][1])
maiorvalor2linha.append(matriz[1][2])
print(f'O maior valor da segunda linha é {max(maiorvalor2linha)}.')'''

#RESOLUÇÃO PROFESSOR

matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz [l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}.')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
