print('Verificador de números primos')
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('Por esse motivo ele é primo!')
else:
    print('Por esse motivo ele não é primo!')
print('''LEGENDA:
[ \033[33mCor Amarela\033[m ] = Número de vezes que ele é divisível.
[ \033[31mCor Vermelha\033[m ] = Números não divisíveis.''')