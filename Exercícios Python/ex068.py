from random import randint

print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-=' * 20)

jog_win = 'GANHOU!'
jogador = 'PAR' , 'IMPAR'
while True:
    if jogador == 'PAR' and jogador == soma % 2 == 0:
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
                print(f'Você {jog_win}')
            elif soma % 1 == 0:
                print('Você PERDEU')        
        if jogador == 'IMPAR':
            if soma % 2 == 0:
                print('Você PERDEU')
            elif soma % 1 == 0:
                print(f'Você {jog_win}')

           

        
        
        