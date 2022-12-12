print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
n1 = int(input('Digite o 1º termo: '))
n2 = int(input('Digite a razão: '))
c = 1
termo = n1
while c <= 10:
    print('{} ->'.format(termo), end='')
    c += 1
    termo += n2
print('Acabou!')