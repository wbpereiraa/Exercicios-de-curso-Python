l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m².'.format(l, a, (a*l)))
print('Para pintar essa parede você precisará de {:.2f}l de tinta.'.format(a*l / 2))
