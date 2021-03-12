valores = input()

valores = valores.split()

# inicio = int(valores[0])
# fim = int(valores[1])

horario = 24 - int(valores[0])
horario = horario + int(valores[1])

if horario > 24:
  horario = horario - 24

print("O JOGO DUROU {} HORA(S)".format(horario))