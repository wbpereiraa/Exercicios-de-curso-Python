from ast import Break
from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade > 18:
    condição = idade - 18
    condição1 = atual - condição
    print('Seu alistamento está atrasado há {} ano(s) e seu alistamento foi em {}.'.format(condição, condição1))
elif idade < 18:
    condição2 = 18 - idade
    condição3 = atual + condição2
    print('Ainda falta {} ano(s) para seu alistamento. Seu alistamento será em {}.'.format(condição2, condição3))

      
    
