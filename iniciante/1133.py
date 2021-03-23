x = int(input())
y = int(input())

maior = x
menor = y

if x < y:
  maior = y
  menor = x


for num in range(menor + 1, maior):
  if num % 5 == 2 or num % 5 == 3:
    print(num)