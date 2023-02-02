#minha solução
aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
if aluno['Média'] < 7 and aluno['Média'] >=5:
    aluno['Situação'] = 'Recuperação'
if aluno['Média'] < 5:
    aluno['Situação'] = 'REPROVADO'
print('-=' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')



