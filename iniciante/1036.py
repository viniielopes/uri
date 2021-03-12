valores = input()

a = float(valores.split()[0])
b = float(valores.split()[1])
c = float(valores.split()[2])

delta = b ** 2 - 4 * a * c

if delta <= 0 or a == 0 or b == 0 or c == 0:
  print("Impossivel calcular")

if delta > 0 and a != 0 and b != 0 and c != 0:
  r1 = (-b + (delta ** 0.5 )) / (2 * a)
  r2 = (-b - (delta ** 0.5)) / (2 * a)

  print("R1 = {:.5f}".format(r1))
  print("R2 = {:.5f}".format(r2))


