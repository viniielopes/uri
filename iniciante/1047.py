valores = input()

valores = valores.split()

horainicio, minutoinicio, horafim, minutofim = map(int, valores)
# minutoinicio = int(valores[1])
# horafim = int(valores[2])
# minutofim = int(valores[3])

minuto = minutofim - minutoinicio

if minuto < 0:
  horafim -= 1
  minutofim += 60
  minuto = minutofim - minutoinicio

horario = 24 - horainicio
horario = horario + horafim

if horario >= 24 and minuto != 0:
  horario -= 24

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horario, minuto))
