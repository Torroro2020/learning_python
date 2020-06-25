figure = input()
if figure == 'треугольник':
    a,b,c = int(input()),int(input()),int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c))**0.5
    print(float(s))
elif figure == 'прямоугольник':
    a, b = int(input()), int(input())
    s = a * b
    print(float(s))
elif figure == 'круг':
    r = int(input())
    s = 3.14 * r**2
    print(s)
