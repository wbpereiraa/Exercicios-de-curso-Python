from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passado...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# programa principal
maior(2, 9, 8, 3, 4, 5, 6)
maior(5, 6, 7, 2)
maior(8, 3, 4)
maior(2, 5)
maior(8)
maior()