princ = [[], []]

for c in range (1,8):
    n = (int(input(f'Digite o {c}º número: ')))
    if n % 2 == 0:
        princ[0].append(n)
    else:
        if n % 2 == 1:
            princ[1].append(n)

#print(princ)
princ[0].sort()
princ[1].sort()

print(f'Os valores pares digitados foram {princ[0]}.')
print(f'Os valores ímpares digitados foram {princ[1]}.')