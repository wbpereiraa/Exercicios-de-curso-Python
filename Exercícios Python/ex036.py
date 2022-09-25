# Programa para empréstimo bancário

Valorcasa = float(input('Qual o valor da casa? R$'))
#print('O valor da casa é de R$ {:.2f}.'.format(Valorcasa))
sal = float(input('Qual o seu salário? R$'))
#print('O seu salário é de R${:.2f}.'.format(sal))
anospag = int(input('Em quantos anos deseja pagar? '))
#print('Você escolheu pagar em {} anos.'.format(anospag))
prestacao = Valorcasa / (anospag * 12)
print('Com isso sua parcela será de R${:.2f} mensais.'.format(prestacao))
if prestacao <= (sal * 0.3):
    print('Parabéns, seu empréstimo foi APROVADO!')
else:
    print('Seu empréstimo foi NEGADO!')







