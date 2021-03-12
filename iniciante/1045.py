valores = input()

valores = valores.split()
i = 0
for numero in valores:
  aux = numero
  j = i
  while j < len(valores):
    if float(aux) < float(valores[j]):
      aux = valores[j]
      valores[j] = valores[i]
      valores[i] = aux
    j+=1
  i+=1
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
if a >= (b + c):
  print("NAO FORMA TRIANGULO")
else:
  if (a ** 2) == (b ** 2 + c ** 2):
    print("TRIANGULO RETANGULO")
  if (a ** 2) > (b ** 2 + c ** 2):
    print("TRIANGULO OBTUSANGULO")
  if (a ** 2) < (b ** 2 + c ** 2):
    print("TRIANGULO ACUTANGULO")
  if a == b and b == c and c == a:
    print('TRIANGULO EQUILATERO')
  if a == b != c or b == c != a or a == c != b:
    print('TRIANGULO ISOSCELES')