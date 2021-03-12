n = int(input())
numeros = []

for i in range(n):
  valor = int(input())
  numeros.append(valor)

dentro = 0 
fora = 0

for num in numeros:
  if num >= 10 and num <= 20:
    dentro += 1
  else:
    fora += 1

print("{} in".format(dentro))
print("{} out".format(fora))