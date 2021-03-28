x = int(input())

while x != 0:
  total = 0
  brake = 0

  for i in range(x, x + 20):
    if i % 2 == 0:
      total += i
      brake += 1

    if brake == 5:
      break
  
  print(total)
  x = int(input())