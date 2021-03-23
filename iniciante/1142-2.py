n = int(input())
num = 1

for i in range(n):
  for j in range(1, 4):
    print("{} ".format(num),end='')

    if j == 3:
      print("PUM", end='')
      num += 1
    num += 1
  print()
