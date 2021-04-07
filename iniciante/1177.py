t = int(input())
aux = 0

for i in range(1000):  
  print("N[{}] = {}".format(i, aux))

  if aux < t -1:
    aux += 1
  else:
    aux = 0
