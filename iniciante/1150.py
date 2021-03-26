x = int(input())

z = int(input())

while z <= x :
  z = int(input())

j = 1
total = x
i = x + 1

while total <= z:
  total = total + i
  j += 1
  i += 1
  
print(j)