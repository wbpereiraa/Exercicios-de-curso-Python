print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)

n = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
print('{} -> {}'.format(a, b), end='')
cont = 3
while cont <= n:
    c = a + b
    print('-> {}'.format(c), end='')
    a = b
    b = c
    cont += 1
print('-> Fim')

