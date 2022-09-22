print('-=' * 25)
print('            Analisador de triângulos')
print('-=' * 25)
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta3 + reta2 > reta1:
    print('Os segmentos acima FORMAM um triângulo.')
else:
    print('Os segmentos acima NÂO FORMAM um triângulo.')


