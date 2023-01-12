lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

#Tuplas são imutaveis

#Técnica 1 (mais clássica)
'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi muito!!')
print(len(lanche))'''

#Técnica 2
'''for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi de mais!')
print(cont)'''

#Técnica 3
'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi de mais!')'''

#print(sorted(lanche)) #Coloca em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))
print(c.count(5))
print(c.index(8))

#pessoa = ('Gustavo', 39, 'M', 99.88)
#print(pessoa[0])
