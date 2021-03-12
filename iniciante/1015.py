import math

plano1 = input()
plano2 = input()

x1, y1 = plano1.split()
x2, y2 = plano2.split()

distancia = math.sqrt(((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2))

print(format(distancia, ".4f"))
