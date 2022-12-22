totG = p1000 = 0
listaP = []
listaProd = []
totalGeral = []
while True:
    nome_produto = str(input('Nome do produto: '))
    listaProd.append(nome_produto) 
    preco = float(input('Preço do produto: R$ '))
    listaP.append(preco)  
    if preco >= 0:
        totG += preco
    if preco > 1000:
        p1000 += 1 
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total gasto da compra é de R$ {totG:.2f}')   
print(f'{p1000} produtos custam mais de R$1000.00.')
while True:
    tupla = (listaP, listaProd)
    totalGeral.append(tupla)
    print(totalGeral)
    break   