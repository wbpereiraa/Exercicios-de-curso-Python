sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválido. Por favor, digite novamente o sexo correspondente [M/F]: ')).strip().upper()[0]
print('Sexo {} incluído com sucesso!'.format(sexo))

