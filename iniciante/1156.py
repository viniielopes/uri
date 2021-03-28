total = 1
i = 3
j = 2

for n in range(1, 101):
  total = total + i/j 
  if i != 39:
    i = i + 2
    j = j + j

  
total = float("{:.1f}".format(total))
print("{:.2f}".format(total))
