km = float(input('Qual a distância da viagem em km? '))
if km <= 200:
    print(' Sua viagem custará R${:.2f}.'.format(km * 0.50))
else:
    print('Sua viagem custará R${:.2f}.'.format(km * 0.45))
print('Obrigado por cotar sua viagem conosco! Boa viagem!')
