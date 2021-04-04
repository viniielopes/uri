n = int(input())

for i in range(n):
  valor = int(input())
  primo = True
  for j in range(2, valor -1):
    if valor % j == 0:
      primo = False
      break

  if primo:
    print("{} eh primo".format(valor))
  else:
    print("{} nao eh primo".format(valor))