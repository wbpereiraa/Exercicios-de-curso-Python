print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro_termo = int(input('Digite o 1º termo: '))
razao_pa = int(input('Digite a razão: '))

ultimo = primeiro_termo + (10-1)*razao_pa

for c in range(primeiro_termo, ultimo + razao_pa, razao_pa):
    print(c, end=' -> ')
print('Acabou!')
   
