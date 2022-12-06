from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa Nasceu? '.format(c)))
    maior_idade = ano_atual - ano
    if maior_idade >= 21:
        totmaior += 1
    elif maior_idade < 21:
        totmenor += 1
print('Ao todo temos {} pessoas menores de idade e {} pessoas maiores de idade.'.format(totmenor, totmaior))

  
        
    
    
    


    
    