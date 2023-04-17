from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado
preço = dado.LeiaDinheiro(input('Digite o preço: R$ '))
moeda.resumo(preço, 80, 35)

