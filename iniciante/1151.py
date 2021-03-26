valores = [0, 1, 1]
n = int(input())

total = 0
prox = 1
ant = 1

i = 4

while i <= n:
  i+= 1
  total = prox + ant
  ant = prox
  prox = total

  valores.append(total)

print(*valores, sep=' ')