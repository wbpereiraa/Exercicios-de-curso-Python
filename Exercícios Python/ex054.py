from datetime import date
soma = 0
for c in range(1,2):
    ano = int(input('Em que ano a {}ª pessoa Nasceu? '.format(c)))
ano_atual = date.today().year
maior_idade = ano_atual - ano
if maior_idade >= 21:
    soma += 1
    print('Temos {} pessoas maiores de idade.'.format(soma))

'''elif maior_idade < 21:
    soma += 1
    print('Temos {} pessoas menores de idade.'.format(soma))'''
    


    
    