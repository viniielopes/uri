# cont = 1

total = 0
coluna_inicio = 0

op = input()

lista = []

for i in range(12):
  linha = []
  for j in range(12):
    valor = float(input())
    linha.append(valor)
    # cont += 1
  # print(linha)
  lista.append(linha)

for index, linha in enumerate(lista):
  # print(index, end=' ')
  for  num in linha[:len(linha) - (len(linha) - coluna_inicio)]:
    # print(num, end=" ")
    total = total + num

  # print()

  if index < 5:
    coluna_inicio += 1
  
  if index > 5:
    coluna_inicio -= 1

if op == 'S':
  print("{:.1f}".format(total))

if op == 'M':
  print("{:.1f}".format(total / 30))