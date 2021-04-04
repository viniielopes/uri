n = int(input())

for i in range(n):

  valores = input()

  valores = valores.split()

  cidadea = int(valores[0])
  cidadeb = int(valores[1])
  crescimentoa = float(valores[2])
  crescimentob = float(valores[3])

  anos = 0

  mensagem = "Mais de 1 seculo."

  while cidadea <= cidadeb:
    cidadea = cidadea + int((cidadea * (crescimentoa / 100)))
    cidadeb = cidadeb + int((cidadeb * (crescimentob / 100)))
    anos += 1
    if anos > 100:
      break

  if anos <= 100:
    mensagem = "{} anos.".format(anos)

  print(mensagem)