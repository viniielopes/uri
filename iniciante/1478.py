valor = -1

while valor != 0:
  valor = int(input())
  if valor == 0:
    break

  for i in range(1, valor + 1):

    for j in range(1, valor + 1):
      menor = i - j + 1

      if j > i:
        menor = j - i + 1

      if j == 1:
        print("{:3d}".format(menor), end='')
      else:
        print("{:4d}".format(menor), end='')

    print()
  print()