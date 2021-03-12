distancia_total = int(input())
combustivel_gasto_litro = float(input())

total_gasto = distancia_total / combustivel_gasto_litro

print(format(total_gasto, ".3f"), "km/l")