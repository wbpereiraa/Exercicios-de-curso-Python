print('{:=^40}'.format(' LOJAS WILL '))
valor_gasto = float(input('Valor total das compras: '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/Cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção de pagamento? '))
if opcao == 1:
    print('Sua compra foi de R${} e vai custar R${} no final.'.format(valor_gasto, valor_gasto - valor_gasto * 0.1))
elif opcao == 2:
    print('Sua compra foi de R${} e vai custar R${} no final.'.format(valor_gasto, valor_gasto - valor_gasto * 0.05))
elif opcao == 3:
    print('Sua compra foi de R${} e vai custar R${} no final.'.format(valor_gasto, valor_gasto))
elif opcao == 4:
    print('Sua compra foi de R${} e vai custar R${} no final.'.format(valor_gasto, valor_gasto + valor_gasto * 0.2))
    
    