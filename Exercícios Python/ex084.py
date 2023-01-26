dados = list()
dados_1 = list()
cont = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    cont += 1
    dados.append(int(input('Digite o peso: ')))
    dados_1.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        break
'''for peso in dados_1:
        if peso[1] >= 100:
        print(f'O maior peso foi de {max(dados_1)}. Peso de {peso[0]}.')
    elif peso[1] <= 70:
        print(f'O menor peso foi de {}. Peso de {peso[0]}.')'''

print(dados_1)
print(f'Foram cadastradas um total de {cont} pessoas.')
print(f'O maior peso foi de {max(dados_1)}Kg.')
print(f'O menor peso foi de {min(dados_1)}Kg.')