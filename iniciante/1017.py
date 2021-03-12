tempo_gasto = int(input())
velocidadeKMh = int(input())

qtd_litro = tempo_gasto * velocidadeKMh / 12

print(format(qtd_litro, ".3f"))