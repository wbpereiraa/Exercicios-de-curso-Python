lista_pesos = [] #Cria uma lista
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa em Kg: '.format(c)))
    lista_pesos.append(peso) #Adiciona os valores digitados a lista
lista_pesos.sort() #organiza a lista na ordem crescente
print('O maior peso lido foi {}KG e o menor peso lido foi {}KG.'.format(lista_pesos[4], lista_pesos[0]))

    