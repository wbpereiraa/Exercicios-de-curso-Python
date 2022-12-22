totG = p1000 = 0
listaGeral = []
while True:
    nome_produto = str(input('Nome do produto: '))
    listaGeral.append(nome_produto) 
    preco = float(input('Preço do produto: R$ '))
    listaGeral.append(preco)  
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
print(listaGeral)        

        