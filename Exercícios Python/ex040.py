n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = float(n1 + n2) / 2
if media >= 7:
    print('Aprovado!')
elif media < 5:
    print('REPROVADO!')        
elif media == 5:
    print('Você está em recuperação!')
elif media <= 6.9:
    print('Você está em recuperação!')