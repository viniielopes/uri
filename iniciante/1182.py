total = 0
coluna_op = int(input())

op = input()

lista = []

for i in range(12):
  linha = []
  for j in range(12):
    valor = float(input())
    linha.append(valor)

  lista.append(linha)

for linha in lista:
  num = linha[coluna_op]
  total = total + num 

if op == 'S':
  print("{:.1f}".format(total))

if op == 'M':
  print("{:.1f}".format(total / 12))