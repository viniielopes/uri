inicio = 7
i = 1
j = 7

while i <= 9 :
  inicio = j + 2
  for index in range(3):
    print("I={} J={}".format(i, j))
    j -= 1

  j = inicio
  i += 2