notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

valor = float(input())

print("NOTAS:")
for nota in notas:
  qtdnota = valor / nota
  valor = valor % nota
  print(int(qtdnota), "nota(s) de R$ {nota:.2f}".format(nota=nota))

print("MOEDAS:")
for moeda in moedas:
  valor = round(valor, 2)
  qtdnota = valor / moeda
  valor = valor % moeda
  print(int(qtdnota), "moeda(s) de R$ {moeda:.2f}".format(moeda=moeda))
