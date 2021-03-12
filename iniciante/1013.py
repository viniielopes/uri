# formula numero maior
# (a + b + c + (a - b - c)) / 2

linha1 = input()
dados1 = linha1.split()

a = int(dados1[0])
b = int(dados1[1])
c = int(dados1[2])

d = (a + b + abs(a - b)) / 2
numero_maior = (c + d + abs(c - d)) / 2

print(int(numero_maior), "eh o maior")