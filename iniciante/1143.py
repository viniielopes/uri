n = int(input())

for i in range(1, n + 1):
  valores = []
  valor = i
  for j in range(1, 4):
    valores.append(valor)
    valor = valor * i 
  print("{0} {1} {2}".format(valores[0], valores[1], valores[2]))