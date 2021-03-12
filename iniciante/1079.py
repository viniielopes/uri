def imprimi_media_ponderada(numeros):
  a = float(numeros[0])
  b = float(numeros[1])
  c = float(numeros[2])

  media_ponderada = (a * 2 + b * 3 + c * 5) / 10
  print("{:.1f}".format(media_ponderada))

x = int(input())

for i in range(x):
  valores = input().split()
  imprimi_media_ponderada(valores)
