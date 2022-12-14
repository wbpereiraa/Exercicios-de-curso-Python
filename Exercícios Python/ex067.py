while True:
    n = int(input('Qual tabuada você deseja visualizar: '))
    if n < 0:
        break
    print('-' * 20)  
    for c in range(1,11): 
        print(f'{n} x {c:2} = {n*c}')
    print('-' * 20)
print('Programa Tabuada finalizado!')

    