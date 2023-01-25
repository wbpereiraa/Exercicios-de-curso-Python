lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'foram digitados {len(lista)} elementos.')