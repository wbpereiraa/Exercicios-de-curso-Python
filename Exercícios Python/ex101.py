'''from datetime import date

def voto():
    if idade >= 16 and idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    elif idade >= 18 and idade < 60:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    elif idade > 60:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    else:
        print(f'Com {idade} anos: NÃO VOTA!')


#programa principal
ano_sistema = date.today().year
nasc = int(input('Em que ano você nasceu: '))
idade = ano_sistema - nasc
voto()'''

#resolução professor
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))