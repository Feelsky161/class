"""#1
side = int(input("Введите размер стороны квадрата: "))
for i in range(side, 0, -1):
    print('* ' * i)
#2
side = int(input("Введите размер стороны: "))
for i in range(1, side + 1):
    print('* ' * i)
#3
side = int(input("Введите размер стороны: "))
for i in range(side):
    print('  ' * i, end='')
    print('* ' * (side - i))
#4
side = int(input("Введите размер стороны: "))
for i in range(side):
    print('  ' * (side - i - 1), end='')
    print('* ' * (i + 1))
#5
side = int(input("Введите размер стороны: "))
for i in range(side - 2, -1, -1):
    print(' ' * (side - i), end='')
    print('* ' * (i + 1))
for i in range(side):
    print(' ' * (side - i), end='')
    print('* ' * (i + 1))"""
#6
#НЕ МОГУ СДЕЛАТЬ.



#7
"""side = int(input("Введите количество звёздочек: "))
for i in range(side):
    print(' ' * (side - i - 1) + '* ' * (i + 1))
for i in range(side - 2, -1, -1):
    print(' ' * (side - i - 1) + '* ' * (i + 1))"""
