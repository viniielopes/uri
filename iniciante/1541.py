import math

while True:
  valor = input()
  valor = valor.split(" ")

  a = int(valor[0])

  if a == 0:
    break

  b = int(valor[1])
  c = int(valor[2])

  area = a * b / (c / 100)
  res = math.sqrt(area)
  res = int(res)

  print(res)