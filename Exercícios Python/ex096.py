def area(l,c):
    area = l * c
    print(f'A área de um terreno {l} x {c} é de {area}m².')

#programa principal
print('Controle de terreno')
print('-' * 20)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l,c)