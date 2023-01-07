from num2words import num2words
n = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

numero = int(input('Digite um número entre 0 e 20: '))
while True:
    if numero >= 0 and numero <= 20:
        
        break
    else:
        numero = int(input('Número inválido! Digite um número entre 0 e 20: '))
num_ptbr = num2words(numero, lang='pt-br')
print(f'Você digitou o número {num_ptbr}.')      