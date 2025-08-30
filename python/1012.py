a, b, c = list(map(float, input().split()))

def triangulo_retangulo(a, c):
    area = (a * c) / 2
    return f'TRIANGULO: {area:.3f}'

def circulo(c):
     pi = 3.14159
     area = pi * (c**2)
     return f'CIRCULO: {area:.3f}'

def trapezio(a, b, c):
     area = (a + b) * c / 2
     return f'TRAPEZIO: {area:.3f}'

def quadrado(b):
     area = b ** 2
     return f'QUADRADO: {area:.3f}'

def retangulo(a, b):
     area = a * b
     return f'RETANGULO: {area:.3f}'


print(triangulo_retangulo(a, c))
print(circulo(c))
print(trapezio(a, b, c))
print(quadrado(b))
print(retangulo(a, b))
