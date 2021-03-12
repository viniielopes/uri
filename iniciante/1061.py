# diainicio = int("Dia 5".split()[1])
# horasinicio = "08 : 12 : 23"

# hora = int(horasinicio.split()[0])
# minuto = int(horasinicio.split()[2])
# segundo = int(horasinicio.split()[4])

# diafinal = int("Dia 5".split()[1])
# horasfinal = "09 : 12 : 22"

# horafinal = int(horasfinal.split()[0])
# minutofinal = int(horasfinal.split()[2])
# segundofinal = int(horasfinal.split()[4])


diainicio = int(input().split()[1])
horasinicio = input()

hora = int(horasinicio.split()[0])
minuto = int(horasinicio.split()[2])
segundo = int(horasinicio.split()[4])

diafinal = int(input().split()[1])
horasfinal = input()

horafinal = int(horasfinal.split()[0])
minutofinal = int(horasfinal.split()[2])
segundofinal = int(horasfinal.split()[4])


segundos_necessario = segundofinal - segundo

if segundos_necessario < 0:
  minutofinal -= 1
  segundofinal += 60
  segundos_necessario = segundofinal - segundo


minutos_necessario = minutofinal - minuto

if minutos_necessario < 0:
  horafinal -= 1
  minutofinal += 60
  minutos_necessario = minutofinal - minuto

horas_necessario = horafinal - hora

if horas_necessario < 0:
  diafinal -= 1
  horafinal += 24
  horas_necessario = horafinal - hora

dia_necessario = diafinal - diainicio

print("{} dia(s)".format(dia_necessario))
print("{} hora(s)".format(horas_necessario))
print("{} minuto(s)".format(minutos_necessario))
print("{} segundo(s)".format(segundos_necessario))