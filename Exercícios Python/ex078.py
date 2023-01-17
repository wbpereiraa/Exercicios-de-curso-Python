
#MINHA SOLUÇÃO!
'''lista = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor: ')))
print(f'Sua lista contem os valores {lista}.')

print(f'O menor valor foi {min(lista)} e ele está na posição {lista.index(min(lista))}.')
print(f'O maior valor foi {max(lista)} e ele está na posição {lista.index(max(lista))}.')'''

#SOLUÇÃO DO PROFESSOR

listanum=[]
mai = 0
men = 0
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para posição {c}: ')))
    if c ==0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'Você digitou os valores {listanum}.')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()