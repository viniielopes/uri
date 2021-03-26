n = int(input())
valores = []

while n != 0:
  valores.clear()
  for i in range(1, n + 1):
    valores.append(i)

  print(*valores, sep=' ')
  n = int(input())