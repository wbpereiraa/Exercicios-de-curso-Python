listacompleta = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um valor: '))
    listacompleta.append(n)
    if n % 2 == 0:
        listapar.append(n)
    if n % 2 != 0:
        listaimpar.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Aqui esta a lista completa com todos os número: {listacompleta}.')
print(f'Aqui esta a lista somente com os números pares: {listapar}.')
print(f'Aqui esta a lista somente com os números impares: {listaimpar}.')