total = 0

x = int(input())
y = int(input())

maior = x
menor = y

if x < y:
  maior = y
  menor = x

for num in range(menor, maior + 1):
  if num % 13 != 0:
    total += num

print(total)