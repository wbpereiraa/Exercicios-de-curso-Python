from random import randint

soma = 0
jogador = str(input('Você quer par ou impar? '))
n = int(input('escolha um número: '))
computador = randint(0,10)
soma = n + computador
print(soma)
if soma % 2 == 0: #jogou par
    soma += computador
    print('Par')
else:
    print('Impar')

        
        
        