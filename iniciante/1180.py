qtd = int(input())
valores = input().split()
valores = list(map(int, valores))


menor = int(valores[0])
pos = 0


for index, valor  in enumerate(valores):
  if menor > valor:
    menor = valor
    pos = index

print("Menor valor: {}".format(menor))
print("Posicao: {}".format(pos))