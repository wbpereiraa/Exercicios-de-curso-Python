p = float(input('Qual o preço do produto? R$'))
print('O produto que custava R${}, na promoção com 5% de desconto vai custar R${:.2f}.'.format(p, p - (p*0.05)))
