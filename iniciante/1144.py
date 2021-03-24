n = int(input())

for i in range(1, n + 1):
  for j in range(0, 2):
    valores = []
    aux = i
    valores.append(i)
    for t in range(2):
      aux = aux * i
      valores.append(aux + j)
    print("{0} {1} {2}".format(valores[0], valores[1], valores[2]))    