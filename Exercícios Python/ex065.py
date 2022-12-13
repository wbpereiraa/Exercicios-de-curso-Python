cont = 0
soma = 0
num = [] #cria a lista
r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input(('Quer continuar? [S/N]'))).upper()
    cont += 1
    soma += n
    num.append(n) #Adiciona itens a lista
    num.sort() #Ordena a lista do maior para o menor
print(num) # Exibe os itens da lista
print('Você digitou {} números e a média entre eles é de {}.'.format(cont, soma / cont))
print('O menor valor foi {} e o maior foi {}.'.format(min(num), max(num)))

    