valores = input()

x = int(valores.split()[0])
y = int(valores.split()[1])

valores = []

for i in range(1, y + 1):
  valores.append(i)

  if len(valores) == x:
    print(*valores, sep=' ')
    valores = []