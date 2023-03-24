def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO. \033[m')
        if ok:
            break
    return valor



#programa principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')