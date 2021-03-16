# x- positivo, y positivo = primeiro quadrante
# x - negativo, y positivo = segundo quadrante
# x - negativo, y negattivo = terceiro quadrante
# x positivo, y negativo = quarto quadrante


x = 1
y = 1

while x != 0 and y != 0:
  valor = input()
  x = int(valor.split()[0])
  y = int(valor.split()[1])

  if x > 0:
    if y > 0:
      print("primeiro")

    if y < 0:
      print("quarto")

  if x < 0:
    if y > 0:
      print("segundo")

    if y < 0:
      print("terceiro")