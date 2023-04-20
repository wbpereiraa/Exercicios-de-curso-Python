def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por Favor digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mERRO! O usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return n
    
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por Favor digite um número Real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mERRO! O usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return n
        
#programa principal
n1 = leiaint('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1} e o real foi {n2}.')