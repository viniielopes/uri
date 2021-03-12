valores = input()

a = int(valores.split()[0])
b = int(valores.split()[1])
c = int(valores.split()[2])
d = int(valores.split()[3])


somacd = c + d
somaab = a + b


if b > c and d > a and somacd > somaab and c > 0 and d > 0 and a % 2 == 0:
  print("Valores aceitos")
else:
  print("Valores nao aceitos")
