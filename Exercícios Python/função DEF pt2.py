#interactive help - ajuda interativa

#help(print)

#print(input.__doc__)

#docstring


'''def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c=i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)'''

'''def somar(a=0,b=0,c=0): #parametros opcionais
    s = a+b+c
    print(f'A soma vale {s}.')

somar(3,2,5)
somar(8,4)
somar()

#escopo de variaveis
#variavel local e variavel global

#programa principal
n = 2
print(f'')'''

'''def funcao():
    n1 = 4 #n1 local
    print(f'N1 dentro vale {n1}')

n1 = 2 #n1 global
print(f'N1 fora vale {n1}')
funcao()'''

#retorno de valores

def somar(a=0,b=0,c=0): 
    s = a+b+c
    return s

r1 = somar(3,2,5)
r2 = somar(8,4)
r3 = somar()
print(f'Os resultador foram {r1}, {r2}, {r3}')


