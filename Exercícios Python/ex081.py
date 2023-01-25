lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
print(f'foram digitados {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'A ordem da lista em ordem decrescente é {lista}.')