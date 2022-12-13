print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
n1 = int(input('Digite o 1º termo: '))
n2 = int(input('Digite a razão: '))
c = 1
termo = n1
total = 0
termos = 10
while termos != 0:
    total = total + termos
    while c <= total:
        print('{} -> '.format(termo), end='')
        c += 1
        termo += n2
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostra a mais? '))
print('Você exibiu ao todo {} termos. Progressão finalizada!'.format(total))