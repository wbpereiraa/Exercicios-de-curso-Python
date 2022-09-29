from datetime import date
atual = date.today().year
sexo = 'F'
sexo = (input('Qual seu sexo? [F] ou [M]? ')).upper()
while sexo =='F':
    print('Alistamento não obrigatório!')
    break
else:
    ano = int(input('Digite o ano de nascimento: '))
    idade = atual - ano
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
    if idade == 18:
        print('Você precisa se alistar IMEDIATAMENTE!')
    if idade > 18:
        condição = idade - 18
        condição1 = atual - condição
        print('Seu alistamento está atrasado há {} ano(s) e seu alistamento foi em {}.'.format(condição, condição1))
    if idade < 18:
        condição2 = 18 - idade
        condição3 = atual + condição2
        print('Ainda falta {} ano(s) para seu alistamento. Seu alistamento será em {}.'.format(condição2, condição3))
    
