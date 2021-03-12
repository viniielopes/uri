PI = 3.14159
linha1 = input()
dados1 = linha1.split()

a = dados1[0]
b = dados1[1]
c = dados1[2]

triangulo = (float(a) * float(c)) / 2
circulo = float(c) ** 2 * PI
trapezio = (float(a) + float(b)) * float(c) / 2
quadrado = float(b) ** 2
retangulo = float(a) * float(b)

print("TRIANGULO:", format(triangulo, ".3f"))
print("CIRCULO:", format(circulo, ".3f"))
print("TRAPEZIO:", format(trapezio, ".3f"))
print("QUADRADO:", format(quadrado, ".3f"))
print("RETANGULO:", format(retangulo, ".3f"))