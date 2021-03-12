coordenadas = input()

x = float(coordenadas.split()[0])
y = float(coordenadas.split()[1])

if x == 0 and y == 0:
  print("Origem")


if x == 0 and y != 0:
  print("Eixo Y")

if x != 0 and y == 0:
  print("Eixo X")
    
if x > 0.0:
  if y < 0.0:
    print("Q4")
  if y > 0.0:
    print("Q1")

if x < 0.0:
  if y < 0.0:
    print("Q3")
  if y > 0.0:
    print("Q2")