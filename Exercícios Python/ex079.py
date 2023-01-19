lista = []

while True:
    num = (int(input('Digite um número para adicionar a lista: ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Você digitou um número repetido. Valor não adicionado! Por favor digite outro numero!')
    r = ''
    r = input('Deseja adicionar outro número? [S/N] ').upper().strip()[0]
    if r == 'N':
        break
print(sorted(lista))