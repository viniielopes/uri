testes = int(input())

for t in range(testes):
  valores = input()

  x = int(valores.split()[0])
  y = int(valores.split()[1])

  total = 0
  brake = 0


  for i in range(x, (x + 10) * y):
    if i % 2 != 0:
      total += i
      brake += 1

    if brake == y:
      break

  print(total)