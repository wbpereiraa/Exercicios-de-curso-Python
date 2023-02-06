dados_trabalhador = {}
from datetime import date

while True:
    dados_trabalhador['Nome'] = str(input('Nome: '))
    dados_trabalhador['Nasc'] = int(input('Nasc: '))
    dados_trabalhador['Sexo'] = str(input('sexo [M/F]: ')).upper()
    ano_atual = date.today().year
    idade = ano_atual - dados_trabalhador['Nasc']
    dados_trabalhador['idade'] = idade
    dados_trabalhador['CTPS'] = int(input('CTPS (0 não tem): '))
    if dados_trabalhador['CTPS'] == 0:
        print('Programa encerrado.')
        break
    if dados_trabalhador['CTPS'] != 0:
        dados_trabalhador['Ano contratação'] = int(input('Ano de contratação: '))
        dados_trabalhador['Salário'] = float(input('Salário: '))

    print('-=' * 55)

    tempo_contribuicaoM = 35 - (ano_atual - dados_trabalhador['Ano contratação'])
    tempo_contribuicaoF = 30 - (ano_atual - dados_trabalhador['Ano contratação'])

    if dados_trabalhador['Sexo'] == 'M':
        if dados_trabalhador['idade'] > 62:
            if ano_atual - dados_trabalhador['Ano contratação'] > 35:
                print('Você já pode se aposentar!')
        else:
            print(f'Você ainda precisa trabalhar mais {62 - dados_trabalhador["idade"]} anos e contrinuir para o INSS por mais {tempo_contribuicaoM} anos para poder se aposentar!')
            

    if dados_trabalhador['Sexo'] == 'F':
        if dados_trabalhador['idade'] > 57:
            if ano_atual - dados_trabalhador['Ano contratação'] > 30:
                print('Você já pode se aposentar!')
        else:
            print(f'Você ainda precisa trabalhar mais {57 - dados_trabalhador["idade"]} anos e contribuir para o INSS por mais {tempo_contribuicaoF} anos poder se aposentar!')
        

    print('-=' * 55)

    for k, i in dados_trabalhador.items():
        print(f'- {k} tem o valor {i}.')
    print('-=' * 55)
    r = 'N'
    r = str(input('Deseja realizar outra análise? [S/N]')).upper().strip()[0]
    if r == 'N':
        print('Programa finalizado!')
        break 
