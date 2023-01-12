n_lista = []
par_lista = []
for c in range(1,5):
    n = int(input(f'Digite o {c}º número: '))
    n_lista.append(n)
    if n % 2 == 0:
        par_lista.append(n)
n_tupla = tuple(n_lista)    
par_tupla = tuple(par_lista)

print(f'Você digitou os números {n_tupla}.')
print(f'O número 9 apareceu {n_tupla.count(9)} vez(es).')

if 3 in n_tupla:
    print(f'O número 3 foi digitado na {n_tupla.index(3)+1}ª posição.')
else:
    print('Não foi digitado nenhum número 3.')
    
print(f'Foram digitados os números pares {par_tupla}.')


