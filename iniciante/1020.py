# 365 - converte para ano
# 30 - converte para mês
# 1 - converte para dia

dias_convertido = []

conversores = [365, 30, 1]

dias = int(input())

for conversor in conversores:
  qtd = dias / conversor
  dias = dias % conversor
  dias_convertido.append(qtd)

print(f'{int(dias_convertido[0])} ano(s)')
print(f'{int(dias_convertido[1])} mes(es)')
print(f'{int(dias_convertido[2])} dia(s)')