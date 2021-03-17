
def notas_validas():    
  valores = []

  while len(valores) != 2:
    valor = float(input())

    if valor < 0 or valor > 10:
      print("nota invalida")
    else:
      valores.append(valor)

  total = valores[0] + valores[1]

  print("media = {:.2f}".format(total / 2))

notas_validas()

novo = 1

while novo != 2:
  print("novo calculo (1-sim 2-nao)")
  novo = int(input())
  if novo == 1:
    notas_validas()
