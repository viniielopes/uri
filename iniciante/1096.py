i = 1
j = 7

while i <= 9 :
  print("I={} J={}".format(i, j))
  j -= 1
  if j == 5:
    print("I={} J={}".format(i, j))
    j = 7
    i += 2