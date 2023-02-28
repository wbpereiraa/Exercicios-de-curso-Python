'''def lin():
    print('-' * 30)

#programa principal
lin()
print('   Curso em vídeo   ')
lin()
lin()
print('   Aprenda Python   ')
lin()
lin()
print('   William Barbosa Pereira   ')
lin()'''

'''def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

#programa principal
mensagem('Curso em vídeo')
mensagem('Aprenda Python')
mensagem('William BArbosa Pereira')'''

'''def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'A soma A + B = {s}')
    print('-' * 30)

#Programa principal
soma(4,5)
soma(8,9)
soma(2,1)
soma(4,5)'''

'''def contador(*num):
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todos {tam} números.')

#programa principal
contador(5,7,3,1,4)
contador(5,4,7)
contador(8,0)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)'''

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')

soma(5,2)
soma(2,9,4)