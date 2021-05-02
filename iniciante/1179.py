par = []
impar = []

for i in range(15):
  valor = int(input())
  
  if valor % 2 == 0:
    par.append(valor)
  
  if valor % 2 != 0:
    impar.append(valor)
  
  if len(par) == 5:
    for i, num in enumerate(par):
      print("par[{}] = {}".format(i, num))
    
    par = []

  if len(impar) == 5:
    for i, num in enumerate(impar):
      print("impar[{}] = {}".format(i, num))
    
    impar = []

if len(impar) > 0:
  for i, num in enumerate(impar):
    print("impar[{}] = {}".format(i, num))

if len(par) > 0:
  for i, num in enumerate(par):
    print("par[{}] = {}".format(i, num))