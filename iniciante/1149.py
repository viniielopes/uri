valores = input()
valores = valores.split()

a = int(valores[0])
pos = 1
total = 0

while int(valores[pos]) <= 0:
  pos += 1

n = int(valores[pos])

for i in range(n):
  total = total + i + a

print(total)