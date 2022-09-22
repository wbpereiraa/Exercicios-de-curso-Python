sal = float(input('Qual é seu salário? R$'))
if sal > 1250:
    print('Você terá um aumento de 10% e seu novo salário será R${:.2f}.'.format((sal * 0.1) + sal))
else:
    print('Você terá um aumento de 15% e seu novo salário será R${:.2f}.'.format((sal * 0.15) + sal))
