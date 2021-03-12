i = 0
j = 1
inicio = 1

while i <= 2 :
  for index in range(3):
    print("I={:g} J={:g}".format(i, j))
    j += 1

  j = float(inicio) + 0.2
  j = float("{:.2f}".format(j))

  inicio = float(inicio) + 0.2
  i = float(i) + 0.2
  i = float("{:.2f}".format(i))