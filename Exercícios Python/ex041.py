from datetime import datetime
print('**********Cadastro CNN**********')
nome = input('Qual é seu nome? ')
ano_nascimento = int(input('Qual o seu ano de nascimento? '))
data_atual = datetime.now()
ano_atual = data_atual.year
idade_atual = ano_atual - ano_nascimento
print('Você tem {} anos.'.format(idade_atual))
categoria = ano_atual - ano_nascimento
if categoria <=  9:
    print('Categoria: MIRIM')
elif categoria > 9 and categoria <= 14:
    print('Categoria: INFANTIL')
elif categoria > 14 and categoria <= 19:
    print('Categoria: JUNIOR')
elif categoria > 19 and categoria <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
    