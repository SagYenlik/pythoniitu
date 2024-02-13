#Exercise 1
side_length = float(input("Введите длину стороны квадрата: "))
perimeter = 4 * side_length
print("Периметр квадрата равен= ", perimeter)

#Exercise 2
side_length = float(input("Введите длину стороны квадрата: "))
square = side_length * side_length
print("Площадь квадрата равна= ", square)

#Exercise 3
side_a = float(input("Введите длину стороны a прямоугольника: "))
side_b = float(input("Введите длину стороны b прямоугольника: "))
square = side_a * side_b
perimeter = 2 * (side_a + side_b)
print("Площадь прямоугольника:", square)
print("Периметр прямоугольника:", perimeter)

#Exercise 4
diameter = float(input("Введите диаметр окружности: "))
pi = 3.14
circumference = pi * diameter
print("Длина окружности:", circumference)

#Exercise 5
side_length = float(input("Введите длину ребра куба: "))
volume = side_length ** 3
surface_area = 6 * (side_length ** 2)
print("Объем куба:", volume)
print("Площадь поверхности куба:", surface_area)

#Exercise 6
a = float(input("Введите длину ребра a: "))
b = float(input("Введите длину ребра b: "))
c = float(input("Введите длину ребра c: "))
volume = a * b * c
surface_area = 2 * (a * b + b * c + a * c)
print("Объем параллелепипеда:", volume)
print("Площадь поверхности параллелепипеда:", surface_area)

#Exercise 7
radius = float(input("Введите радиус окружности: "))
pi = 3.14
circumference = 2 * pi * radius
area = pi * radius ** 2
print("Длина окружности:", circumference)
print("Площадь круга:", area)

#Exercise 8
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
average= (a+b)/2
print("Среднее арифметическое:", average)

#Exercise 9
import math
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
geo_mean = math.sqrt(a * b)
print("Среднее геометрическое чисел: ", geo_mean)

#Exercise 10
a = float(input("Введите число a, не равное нулю: "))
b = float(input("Введите число b, не равное нулю: "))
if a == 0 or b == 0:
    print("Ошибка: одно из чисел равно нулю.")
else:
    a_squared = a ** 2
    b_squared = b ** 2
    sum = a_squared + b_squared
    difference = a_squared - b_squared
    product = a_squared * b_squared
    division = a_squared / b_squared
    print("Сумма квадратов:", sum)
    print("Разность квадратов:", difference)
    print("Произведение квадратов:", product)
    print("Частное квадратов:", division)

#Exercise 11
a = float(input("Введите число a, не равное нулю: "))
b = float(input("Введите число b, не равное нулю: "))
if a == 0 or b == 0:
    print("Ошибка: одно из чисел равно нулю.")
else:
    abs_a = abs(a)
    abs_b = abs(b)
    sum = abs_a + abs_b
    difference = abs_a - abs_b
    product = abs_a * abs_b
    division = abs_a / abs_b
    print("Сумма модулей:", sum)
    print("Разность модулей:", difference)
    print("Произведение модулей:", product)
    print("Частное модулей:", division)
    
#Exercise 12
import math
a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))
c = math.sqrt(a**2 + b**2)
perimeter = a + b + c
print("Гипотенуза треугольника:", c)
print("Периметр треугольника:", perimeter)

#Exercise 13
R1 = float(input("Введите радиус круга R1 (R1 > R2): "))
R2 = float(input("Введите радиус круга R2: "))
pi = 3.14
if R1 <= R2:
    print("Ошибка: R1 должен быть больше R2.")
else:
    S1 = pi * (R1 ** 2)
    S2 = pi * (R2 ** 2)
    S3 = S1 - S2
    print("Площадь круга S1:", S1)
    print("Площадь круга S2:", S2)
    print("Площадь кольца S3:", S3)

#Exercise 14
L = float(input("Введите длину окружности L: "))
pi = 3.14
R = L / (2 * pi)
S = pi * (R ** 2)
print("Радиус окружности R:", R)
print("Площадь круга S:", S)

#Exercise 15
import math
S = float(input("Введите площадь круга S: "))
pi = 3.14
R = math.sqrt(S / pi)
D = 2 * R
L = 2 * pi * R
print("Диаметр круга D:", D)
print("Длина окружности L:", L)

#Exercise 16
x1 = float(input("Введите координату x1: "))
x2 = float(input("Введите координату x2: "))
distance = abs(x2 - x1)
print("Расстояние между точками:", distance)

#Exercise 17
A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C: "))
length_AC = abs(C - A)
length_BC = abs(C - B)
sum = length_AC + length_BC
print("Длина отрезка AC:", length_AC)
print("Длина отрезка BC:", length_BC)
print("Сумма длин отрезков AC и BC:", sum)

#Exercise 18
A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C: "))
if A < C < B or B < C < A:
    length_AC = abs(C - A)
    length_BC = abs(B - C)
    product_lengths = length_AC * length_BC
    print("Произведение длин отрезков AC и BC:", product_lengths)
else:
    print("Точка C не находится между точками A и B")

#Exercise 19
x1 = float(input("Введите координату x1: "))
y1 = float(input("Введите координату y1: "))
x2 = float(input("Введите координату x2: "))
y2 = float(input("Введите координату y2: "))
length = abs(x2 - x1)
width = abs(y2 - y1)
perimeter = 2 * (length + width)
area = length * width
print("Периметр прямоугольника:", perimeter)
print("Площадь прямоугольника:", area)

#Exercise 20
import math
x1 = float(input("Введите координату x1: "))
y1 = float(input("Введите координату y1: "))
x2 = float(input("Введите координату x2: "))
y2 = float(input("Введите координату y2: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Расстояние между точками:", distance)
