from collections import Counter
resposta = 'S'
i = []
s = []
maior_18 = []
homens = []
mulher_20 = []
soma_i = 0
soma_s = 0
while resposta == 'S':
    idade = int(input('Digite a idade: '))
    i.append(idade)
    if idade > 18:
        maior_18.append(idade)
    if idade < 20:
        mulher_20.append(idade)
    sexo = str(input('Digite o sexo: [M/F]: ')).upper().strip()[0]
    s.append(sexo)
    if sexo == 'M':
        homens.append(sexo)
    if sexo == 'F':
        mulher_20.append(sexo)
    resposta = str(input('Deseja continuar o cadastro [S/N]? ')).upper().strip()[0]
    
print(maior_18)
print(homens)
print(mulher_20)
print(f'{(len(maior_18))} pessoas tem mais de 18 anos de idade!')
print(f'{(len(homens))} homens foram cadastrados!')
#usando o método counter() IMPORTANDO A BIBLIOTECA COLLECTIONS (COUNTER)
x = 'F' #define qual elemento vai ser buscado na lista
c = Counter(mulher_20) #define a lista que será contada o elemento definido
print(f'{c[x]} mulheres tem menos de 20 anos!') #exibe o elemento da lista quantas vezes se repetiu.
