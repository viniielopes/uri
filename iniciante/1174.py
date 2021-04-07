i = 0

while i <= 99:
  valor = float(input())

  if valor <= 10:
    print("A[{}] = {:.1f}".format(i, valor))
  i = i + 1