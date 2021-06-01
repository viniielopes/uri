# cont = 1

total = 0
coluna_op = 1

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

for linha in lista:
  for num in linha[:len(linha) - coluna_op]:
    # print(num)
    total = total + num 
  coluna_op += 1

if op == 'S':
  print("{:.1f}".format(total))

if op == 'M':
  print("{:.1f}".format(total / 66))