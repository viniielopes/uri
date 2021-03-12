valores = input()

n1 = float(valores.split()[0]) * 2
n2 = float(valores.split()[1]) * 3
n3 = float(valores.split()[2]) * 4
n4 = float(valores.split()[3]) * 1


media = (n1+n2+n3+n4 )/ 10

print("Media: {:.1f}".format(media))

if media >= 7.0:
  print("Aluno aprovado.")

if media < 5.0:
  print("Aluno reprovado.")

if media >=5.0 and media <=6.9:
  print("Aluno em exame.")
  media_exame = float(input())
  print("Nota do exame: {:.1f}".format(media_exame))

  media_final = (media + media_exame )/ 2
  if media_final <=4.9:
    print("Aluno reprovado.")
  else:
    print("Aluno aprovado.")

  print("Media final: {:.1f}".format(media_final))
