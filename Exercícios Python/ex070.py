totG = p1000 = menor = cont = 0
barato = ' '
listaP = []
listaProd = []
totalGeral = []
while True:
    nome_produto = str(input('Nome do produto: '))
    listaProd.append(nome_produto) 
    preco = float(input('Preço do produto: R$ '))
    listaP.append(preco)  
    cont += 1
    if preco >= 0:
        totG += preco
    if preco > 1000:
        p1000 += 1 
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome_produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total gasto da compra é de R$ {totG:.2f}')   
print(f'{p1000} produtos custam mais de R$1000.00.')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')