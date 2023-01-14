palavras = ('arroz','batata', 'carro', 'danone', 'escola', 'feijao', 
            'gato', 'historia', 'igreja', 'jesus', 'kiko', 'lapis', 'mato', 'nuvem', 
            'opera', 'pato', 'queijo', 'rato', 'sapo', 'tatu', 'uva', 'vivo', 'william', 'xuxa', 'yvone', 'zebra')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')