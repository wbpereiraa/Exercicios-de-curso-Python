peso = float(input('Qual o seu peso? (KG)'))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura**2)
print('O IMC desta pessoa é {:.2f}.'.format(imc))
if imc < 18.5:
    print('ATENÇÃO! Você esta abaixo do Peso!')
if 18.5 <= imc < 25:
    print('Você esta no Peso ideal!')
if 25 <= imc < 30:
    print('Você esta com Sobrepeso!')
if 30 <= imc < 40:
    print('Você esta com Obesidade!')
elif imc >= 40:
    print('ATENÇÃO! Você esta com Obesidade Mórbida!')
    
        