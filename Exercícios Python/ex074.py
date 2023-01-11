import random
random_numbers = random.sample(range(10), 5)
minha_tupla = tuple(random_numbers)
print('Os valores sorteados são: ' , end='')
print(minha_tupla)
print(f'O menor número gerado foi {min(minha_tupla)}.')
print(f'O maior número gerado foi {max(minha_tupla)}.')
