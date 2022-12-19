from random import randint

print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-=' * 20)

cont = 0
jogador = 'PAR' , 'IMPAR'
while cont == cont:
    jogador = str(input('Você quer par ou impar? ')).upper()
    n = int(input('escolha um número: '))
    print('-' * 20)
    computador = randint(0,10)
    soma = n + computador
    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} deu par!')
    else:
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} deu impar!')
    if jogador == 'PAR':
        if soma % 2 == 0:
            print('Você GANHOU!')
            cont += 1
        elif soma % 1 == 0:
            print('Você PERDEU')
            break      
    if jogador == 'IMPAR':
        if soma % 2 == 0:
            print('Você PERDEU')
            break
        elif soma % 1 == 0:
            print('Você GANHOU')
            cont += 1
    print('Vamos jogar novamente...')
print(f'Gamer Over! Você venceu {cont} vezes.')



           

        
        
        