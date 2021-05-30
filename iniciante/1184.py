total = 0
coluna_op = 0

op = input()

lista = []

for i in range(12):
  linha = []
  for j in range(12):
    valor = float(input())
    linha.append(valor)
  lista.append(linha)

for linha in lista:
  for num in linha[:coluna_op]:
    total = total + num 
  coluna_op += 1

if op == 'S':
  print("{:.1f}".format(total))

if op == 'M':
  print("{:.1f}".format(total / 66))