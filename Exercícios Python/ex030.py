numero = int(input('Digite um número: '))
resultado = numero % 2
#print('O resultado foi {}.'.format(resultado))
if resultado == 1:
    print('O número {} é Ímpar.'.format(numero))
else:
    print('O número {} é Par.'.format(numero))
