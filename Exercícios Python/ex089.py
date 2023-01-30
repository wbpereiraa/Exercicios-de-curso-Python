lista_geral = []

while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input(f'Digite a nota: '))
    nota2 = float(input(f'Digite a nota: '))
    media = (nota1 + nota2)/2
    lista_geral.append([aluno,[nota1, nota2], media])
    r = 'N'
    r = str(input('Deseja continuar: [S/N]')).upper().strip()[0]
    if r == 'N':
        break
print('-=' * 30)
print(f'{"No":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)

for i, a, in enumerate(lista_geral):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('programa finalizado!')
        break
    if opc <= len(lista_geral) - 1:
        print(f'Notas de {lista_geral[opc][0]} são {lista_geral[opc][1]}')

