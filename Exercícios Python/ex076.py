        #Resolução do professor

listagem = ('Celular', 3500, 
            'Computador', 2400,
            'Mouse', 175.00, 
            'Fone de ouvido', 499.00, 
            'Cadeira gamer', 1200, 
            'Mouse pad', 125.00)
print('-' * 40)
print(f'{"Listagemn de preços":^40}')
print('-' * 40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = ' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)





