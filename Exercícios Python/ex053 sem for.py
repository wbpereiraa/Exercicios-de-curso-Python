frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # cria uma lista com a frase ex:['A','aranha','é','marrom']
junto = ''.join(palavras) # tira os espaços da frase ex: Aaranhaémarrom
inverso = junto[::-1] # inverte a frase ex: morraméahnaraA
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')