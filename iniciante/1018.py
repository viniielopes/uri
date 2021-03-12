notas = [100, 50, 20, 10, 5, 2, 1]

valor = int(input())

print(valor)

for nota in notas:
  qtdnota = valor / nota
  valor = valor % nota
  print(int(qtdnota), "nota(s) de R$ {nota},00".format(nota=nota))
