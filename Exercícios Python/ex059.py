from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos Números
        [ 5 ] Sair do Programa
        ''')
    opcao = int(input('Digite uma das opções acima: '))
    if opcao == 1:
        print('A soma entre {} + {} é igual a {}.'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A Multiplicação entre {} x {} é igual a {}.'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é {}.'.format(n1, n2, n1 ))
        else:
            print('O maior número entre {} e {} é {}.'.format(n1, n2, n2))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizando....')
        sleep(3)      
    else:
        print('Opção inválida. Tente novamente!') 
    sleep(1)
    print('='*40)
print('Fim do programa! Volte sempre!') 