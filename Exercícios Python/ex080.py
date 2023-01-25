valores = list()
for cont in range(0,5):
    num = (int(input('Digite um valor: ')))  
    if cont == 0 or num > valores[-1]: # pega o 1º e o ultimo valor.
        valores.append(num)
        print('Adicionado ao final da lista.')
    else:
        pos = 0 #começa na posiççao zero
        while pos < len(valores): #percorre a lista
            if num <= valores[pos]:
                valores.insert(pos,num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1 
print(f'Os valores digitados em ordem foram {valores}.')



