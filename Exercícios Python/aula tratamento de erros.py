try:
    a = int(input('Digite o número: '))
    b = int(input('Digite o denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possivel dividir por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}!')
else:
    print(f'O resultado é {r:.2f}.')
finally:
    print('Obrigado, Volte sempre!')