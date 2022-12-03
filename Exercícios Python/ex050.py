soma = 0
print('Somando numeros inteiros pares: ')
for num in range(1, 7):
    valor = int(input('Digite o {}º valor: '.format(num)))
    if valor % 2 == 0:
        soma += valor
print('A soma dos números inteiro pares é igual a {}.'.format(soma))

