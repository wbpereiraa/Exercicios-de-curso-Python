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
    sexo = str(input('Digite o sexo: [M/F]: ')).upper().strip()[0]
    s.append(sexo)
    if sexo == 'M':
        homens.append(sexo)
    if idade < 20 and sexo == 'F':
        mulher_20.append()
    resposta = str(input('Deseja continuar o cadastro [S/N]? ')).upper().strip()[0]
print(i)
print(s)
