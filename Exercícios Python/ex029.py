velocidade = float(input('Qual a velocidade que o carro estava? '))
if velocidade > 80:
    print('Você ultrapassou o limite permitido que é de 80km/h!')
    print('Você foi multado em R${:.2f}. DIRIJA COM MAIS CUIDADO!'.format((velocidade - 80) * 7))
    print('Sua vida não tem preço!')
else:
    print('Você não foi multado, tenha um Bom dia e dirija com segurança!!')
