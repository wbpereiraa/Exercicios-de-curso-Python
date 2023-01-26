dados = list()
dados_1 = list()
cont = 0
mai = men = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    cont += 1
    dados.append(float(input('Digite o peso: ')))
    if len(dados_1) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    dados_1.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        break

#print(dados_1)
print(f'Foram cadastradas um total de {cont} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de', end=' ')
for p in dados_1:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de', end=' ')
for p in dados_1:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()