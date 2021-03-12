# 3600 - converte para hora
# 60 - converte para minuto

horario_convertido = []

conversores = [3600, 60, 1]

segundos = int(input())

for conversor in conversores:
  qtd = segundos / conversor
  segundos = segundos % conversor
  horario_convertido.append(qtd)

print(f'{int(horario_convertido[0])}:{int(horario_convertido[1])}:{int(horario_convertido[2])}')